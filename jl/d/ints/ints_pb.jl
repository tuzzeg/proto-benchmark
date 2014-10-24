module ints


using ProtoBuf
import ProtoBuf.meta

type Ints1
    i1::Int32
    i2::Int64
    i3::Uint32
    i4::Uint64
    i5::Int32
    i6::Int64
    i7::Uint32
    i8::Uint64
    Ints1() = (o=new(); fillunset(o); o)
end #type Ints1
const __req_Ints1 = Symbol[:i1,:i2,:i3,:i4]
meta(t::Type{Ints1}) = meta(t, __req_Ints1, ProtoBuf.DEF_FNUM, ProtoBuf.DEF_VAL, true, ProtoBuf.DEF_PACK)

export Ints1
export meta
end # module ints
