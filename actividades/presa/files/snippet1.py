mesh = meshio.read("files/dam_param.msh")
points = mesh.points
cells  = mesh.cells
cell_data  = mesh.cell_data
aux.script_mesh(mesh)