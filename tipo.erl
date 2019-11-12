-module(tipo).
-compile([export_all]).
tri(A, B, C) when A =< 0 ->
  "las medidas no pueden ser 0";
tri(A, B, C) when B =< 0 ->
  "las medidas no pueden ser 0";
tri(A, B, C) when C =< 0 ->
  "las medidas no pueden ser 0";
tri(A, B, C) when A == B, A /= C ->
  isosceles;
tri(A, B, C) when B /= A , B == C ->
  isosceles;
tri(A, B, C) when A == C, A /= B ->
  isosceles;
tri(A, B, C) when A == B, A == C ->
  equilatero;
tri(A, B, C) when B == C, A == B ->
  equilatero;
tri(A, B, C) when C == A, C == B ->
    equilatero;
tri(A, B, C) when A /= B, A /= C, B /= C ->
  escaleno.
