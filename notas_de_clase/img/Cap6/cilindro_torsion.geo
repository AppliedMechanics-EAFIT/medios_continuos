// Puntos
Point(1) = {0, 0, 0, 1};
Point(2) = {1, 0, 0, 1};
Point(3) = {0, 1, 0, 1};
Point(4) = {-1, 0, 0, 1};
Point(5) = {0, -1, 0, 1};


// Arcos
Circle(1) = {2, 1, 3};
Circle(2) = {3, 1, 4};
Circle(3) = {4, 1, 5};
Circle(4) = {5, 1, 2};

// Extrusion
Extrude {0, 0, 5} {
  Line{1, 2, 3, 4};
}


// Subdivision
ndiv_arco = 5;
ndiv_altura = 5;
Transfinite Line {1, 2, 3, 4, 9, 13, 5, 17} = ndiv_arco Using Progression 1;
Transfinite Line {6, 7, 11, 15} = ndiv_altura Using Progression 1;
Transfinite Surface {8};
Transfinite Surface {12};
Transfinite Surface {16};
Transfinite Surface {20};
Recombine Surface {8, 12, 16, 20};


// Tapa
Line Loop(1) = {9, 13, 17, 5};
Plane Surface(21) = {1};
Transfinite Surface {21};
