using ProtoBuf

include("d/ints/ints_pb.jl")

macro timeit(ntrials, ex)
  quote
    t = 0.0
    for i=0:$(esc(ntrials))
      e = 1000*(@elapsed $(esc(ex)))
      if i > 0
        # warm up on first iteration
        t += e
      end
    end
    t
  end
end

function read_file(file::String)
  raw_protos = Array(Array{Uint8,1}, 0)

  open(file, "r") do f
    while !eof(f)
      buf = readbytes(f, 4)
      if length(buf) < 4
        break
      end
      size = buf[1] | buf[2]<<8 | buf[3]<<16 | buf[4]<<24

      buf = readbytes(f, size)
      if length(buf) < size
        break
      end
      push!(raw_protos, buf)
    end
  end
  raw_protos
end

function parse_protos{T}(protos::Array{Array{Uint8,1},1}, ::Type{T})
  for buf in protos
    proto = T()
    readproto(IOBuffer(buf), proto)
  end
end

immutable Args
  file::String
  repeats::Int
end

function parse_args()
  file = ""
  repeats = 1

  for i in 1:length(ARGS)
    if ARGS[i] == "--count"
      i += 1
      repeats = int(ARGS[i])
    elseif ARGS[i] == "--file"
      i += 1
      file = ARGS[i]
    end
  end

  Args(file, repeats)
end

function main()
  args = parse_args()
  file = args.file
  repeats = args.repeats

  raw_protos = read_file(file)

  ms = @timeit repeats parse_protos(raw_protos, ints.Ints1)
  println("{\"library\": \"julia/ProtoBuf\", \"file\": \"$file\", \"count\": $repeats, \"time-millis\": $ms}\n");
end

main()
