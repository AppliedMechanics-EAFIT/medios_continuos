// Gmsh project created on Thu Mar 22 18:44:27 2018


Point(1) = {0, 0, 0, 1.0};
Point(2) = {1, 0, 0, 1.0};
Point(3) = {1, 1, 0, 1.0};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 1};

Line Loop(1) = {2, 3, 1};
Plane Surface(1) = {1};
