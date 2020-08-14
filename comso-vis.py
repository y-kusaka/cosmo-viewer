import re, os
from io import StringIO
import pandas
import numpy as np
import open3d as o3d # should be the latest build (official release of 0.10.0 does not support .orient_normals_consistent_tangent_plane)
import pyvista as pv # used only for visualization

def to_pointCloud():
	# parse the COSMO file and get metadata
	df = get_seg_DataFrame(COSMO_contents)
	xyz = df.loc[:, ["x / a.u.", "y / a.u.", "z / a.u."]].values #x, y, z
	v = df["charge/area / e/A^2"].values # charge / area


