project(Persistence_representations_example)

#This is an additional line in which we are adding to compilation the file we need to
#experiment with the landom point clouds.
add_executable ( study_of_random_point_cloud_in_different_dimensions study_of_random_point_cloud_in_different_dimensions.cpp )
if (TBB_FOUND)
  target_link_libraries(study_of_random_point_cloud_in_different_dimensions ${TBB_LIBRARIES})
endif()

add_executable ( Persistence_representations_example_landscape_on_grid persistence_landscape_on_grid.cpp )
add_test(NAME Persistence_representations_example_landscape_on_grid
    COMMAND $<TARGET_FILE:Persistence_representations_example_landscape_on_grid>)
install(TARGETS Persistence_representations_example_landscape_on_grid DESTINATION bin)

add_executable ( Persistence_representations_example_landscape persistence_landscape.cpp )
add_test(NAME Persistence_representations_example_landscape
    COMMAND $<TARGET_FILE:Persistence_representations_example_landscape>)
install(TARGETS Persistence_representations_example_landscape DESTINATION bin)

add_executable ( Persistence_representations_example_intervals persistence_intervals.cpp )
add_test(NAME Persistence_representations_example_intervals
    COMMAND $<TARGET_FILE:Persistence_representations_example_intervals>
    "${CMAKE_SOURCE_DIR}/data/persistence_diagram/first.pers")
install(TARGETS Persistence_representations_example_intervals DESTINATION bin)

add_executable ( Persistence_representations_example_vectors persistence_vectors.cpp )
add_test(NAME Persistence_representations_example_vectors
    COMMAND $<TARGET_FILE:Persistence_representations_example_vectors>)
install(TARGETS Persistence_representations_example_vectors DESTINATION bin)

add_executable ( Persistence_representations_example_heat_maps persistence_heat_maps.cpp )
add_test(NAME Persistence_representations_example_heat_maps
    COMMAND $<TARGET_FILE:Persistence_representations_example_heat_maps>)
install(TARGETS Persistence_representations_example_heat_maps DESTINATION bin)

