#include <cstdio>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>
#include <chrono>

#include "ints.pb.h"

using namespace std;

const size_t unpack_size(const char buf[]) {
  size_t l = buf[0] | (buf[1]<<8) | (buf[2]<<16) | (buf[3]<<24);
  return l;
}

// Read serialized protos as strings from delimited file
// File format:
//   <size_1::4 bytes><string_1::size_1 bytes><size_2::4 bytes><string_2::size_2 bytes>...
void read_protos(const char* file_name, vector<string> &raw_protos) {
  fstream in(file_name, ios::in | ios::binary);

  char buf[4];
  char proto_buf[1024];

  while (!in.eof()) {
    in.read(buf, 4);
    if (!in) {
      break;
    }
    const size_t l = unpack_size(buf);
    in.read(proto_buf, l);
    if (!in) {
      break;
    }
    raw_protos.push_back(string(proto_buf, l));
  }

  in.close();
}

typedef struct args {
  unsigned long repeats;
  char file[1024];

  args() : repeats(0), file("") {}
} args_t;

void parse_args(int argc, char* argv[], args_t* args) {
  for (int i = 1; i < argc; ++i) {
    if (strcmp(argv[i], "--count") == 0) {
      ++i;
      sscanf(argv[i], "%lu", &args->repeats);
    } else if (strcmp(argv[i], "--file") == 0) {
      ++i;
      sscanf(argv[i], "%s", args->file);
    }
  }
}

int main(int argc, char* argv[]) {
  args_t args;
  parse_args(argc, argv, &args);
  printf("file=%s\n", args.file);

  vector<string> raw_protos;
  read_protos(args.file, raw_protos);

  GOOGLE_PROTOBUF_VERIFY_VERSION;

  const chrono::high_resolution_clock::time_point t0 = chrono::high_resolution_clock::now();

  ints::Ints1 proto;
  for (int i = 0; i < args.repeats; ++i) {
    for (vector<string>::iterator it = raw_protos.begin(); it != raw_protos.end(); ++it) {
      proto.ParseFromString(*it);
    }
  }

  const chrono::high_resolution_clock::time_point t1 = chrono::high_resolution_clock::now();
  const unsigned long ms = chrono::duration_cast<std::chrono::microseconds>(t1-t0).count();

  printf("{\"library\": \"protobuf-c\", \"count\": %lu, \"time-millis\": %lu}\n", args.repeats*raw_protos.size(), ms);
}
