
import ifcopenshell

# Open the IFC file
ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")

# Confirm if the IFC file is loaded
print("IFC file loaded:", ifc_file.schema)


# PROJECT NAME 
# Get the IfcProject entity (the root of the model)
project = ifc_file.by_type("IfcProject")[0]
print("Project Name:", project.Name)
print()

# List Stairs
stairs = ifc_file.by_type("IfcStair")
print(f"No. of Stairs: {len(stairs)}")

# Data from Stairs
for stair in stairs:
    print(stair.GlobalId, stair.Name)


# List Slabs
slabs = ifc_file.by_type("IfcSlab")
print(f"No. of Slabs: {len(slabs)}")

# Data from slabs & Renaming of Slabs
for i, slab in enumerate(slabs, 1):
    slab.Name = f"Renamed_Slab_{i}"
    print(f"Updated Slab: {slab.GlobalId} -> {slab.Name}")
print()

# Print name and Elevation of Each Floor
# project = ifc_file.by_type("IfcProject")[0]
print("Spatial Structure:")
# Navigating through the project spacce by space
# Inside of the first IFC Project, we will access ALL and each site
for site in project.IsDecomposedBy[0].RelatedObjects:
    # Inside if the each site, we will access ALL and each building
    for building in site.IsDecomposedBy[0].RelatedObjects:
        # Inside of each building, we will access ALL and each buildingstorey
        for storey in building.IsDecomposedBy[0].RelatedObjects:
            print("Storey", storey.Name, "Elevation", storey.Elevation)

print()


#List all objects
types = set(el.is_a() for el in ifc_file)
print("Object types in file:", types)
#do i or do i not print in loop????
#   for type in types:
#       print(type)
print()


# Save as new ifc file
new_filename = "AC20-FZK-Haus_renamed.ifc"
ifc_file.write(new_filename)
print(f"Saved renamed slabs to: {new_filename}")
