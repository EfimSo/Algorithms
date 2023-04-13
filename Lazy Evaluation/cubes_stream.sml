(* ****** ****** *)
(*Stream datatype constructors*)

datatype 'a strcon =
  strcon_nil
| strcon_cons of
  ('a * (unit -> 'a strcon))

type 'a stream = (unit -> 'a strcon)

(* ****** ****** *)


(*
//
Enumerates all the pairs (i, j) of natural
numbers satisfying $i <= j$; a pair (i1, j1) must
be enumerated ahead of another pair (i2, j2) if the
following condition holds:
  i1*i1*i1 + j1*j1*j1 < i2*i2*i2 + j2*j2*j2
//
*)

fun cube_sum(ij) = 
    let
      val (i, j) = ij
    in
      i*i*i + j*j*j
    end

fun cube_sum_lte(ij1, ij2) = 
    cube_sum(ij1) <= cube_sum(ij2)

fun str_merge(fx1, fx2, lte3) = fn() =>
    let
      val strcon_cons(x1, xs1) = fx1()
      val strcon_cons(x2, xs2) = fx2()
    in
      if lte3(x1, x2) then 
        strcon_cons(x1, str_merge(xs1, fx2, lte3))
      else
        strcon_cons(x2, str_merge(fx1, xs2, lte3))
    end


val
theNatPairs_cubesum: (int * int) stream = fn () => 
  let
    fun pair_stream(i, j) = fn() => strcon_cons((i, j), pair_stream(i, j+1))
    fun helper(i) = fn() =>
        strcon_cons((i, i), str_merge(pair_stream(i, i+1), helper(i+1), cube_sum_lte))
  in
    helper(0)()
  end

(* ****** ****** *)

(* end of [CS320-2023-Spring-assign07-02.sml] *)
