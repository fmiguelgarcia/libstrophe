set( EXAMPLE_LIBRARIES strophe -lresolv )

add_executable( basic basic.c )
target_link_libraries( basic ${EXAMPLE_LIBRARIES} )

add_executable( bot bot.c )
target_link_libraries( bot ${EXAMPLE_LIBRARIES} )

add_executable( active active.c )
target_link_libraries( active ${EXAMPLE_LIBRARIES} )

add_executable( component component.c )
target_link_libraries( component ${EXAMPLE_LIBRARIES} )

add_executable( roster roster.c )
target_link_libraries( roster ${EXAMPLE_LIBRARIES} )

add_executable( uuid uuid.c )
target_link_libraries( uuid ${EXAMPLE_LIBRARIES} )

