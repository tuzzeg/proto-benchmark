CXX = g++
CXXFLAGS = -Wall -g

t/ints.pb.o: cc/d/ints/ints.pb.cc cc/d/ints/ints.pb.h
	$(CXX) $(CXXFLAGS) -o t/ints.pb.o -c cc/d/ints/ints.pb.cc -I/usr/local/include -Icc

t/parse.o: cc/parse.cc
	$(CXX) $(CXXFLAGS) -o t/parse.o -c cc/parse.cc -I/usr/local/include -Icc/d/ints

cc_parse: t/parse.o t/ints.pb.o
	$(CXX) $(CXXFLAGS) -o cc_parse t/parse.o t/ints.pb.o -L/usr/local/lib -lprotobuf
