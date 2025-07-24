# import arcpy

# feature_class = "Highways"
# field_name = "HWY_SYMBOL"

# # Check if the field exists before calculation
# field_names = [field.name for field in arcpy.ListFields(feature_class)]

# if field_name in field_names:
#     # Append 'Highway' with the existing field value
#     expression = "'Highway ' + str(!{}!)".format(field_name)
#     arcpy.management.CalculateField(
#         in_table=feature_class,
#         field=field_name,
#         expression=expression,
#         expression_type="PYTHON3"
#     )
# else:
#     print(f"Field '{field_name}' not found.")
print ("ArcPy")