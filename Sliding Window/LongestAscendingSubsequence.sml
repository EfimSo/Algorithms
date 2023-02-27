(*
Given a list of integers xs,
please implement a function that find
the longest ascending subsequence of xs.
If there are more than one such sequences,
the left most one should be returned.
*)


fun list_longest_ascend(xs: int list): int list = 
    let
        fun loop(xs: int list, max_acc: int list, curr_acc: int list) = 
            let
                val x1 = case curr_acc of 
                                  nil => NONE
                                  | h :: t => SOME(h)
                fun length(xs: int list): int = 
                    let
                        fun loop(xs: int list, acc: int) = 
                            case xs of 
                                nil => 0
                                | h :: t => loop(t, acc + 1)    
                    in 
                        loop(xs, 0)
                    end
            in
            case xs of 
                nil => max_acc
                | h :: t => case x1 of 
                                NONE => loop(t, max_acc, [h])
                                | SOME x => 
                                  if h <= x then loop(t, max_acc, [h])
                                  else loop(t, (if (length(curr_acc) + 1) > length(max_acc) then h :: curr_acc else max_acc), h :: curr_acc)
            end
            fun rappend(xs: int list, ys: int list): int list = 
                case xs of 
                    nil => ys
                    | h :: t => rappend(t, h :: ys)
    in
        rappend(loop(xs, [], []), [])
    end


(* ****** ****** *)

(* end of [CS320-2023-Spring-assign03-04.sml] *)
