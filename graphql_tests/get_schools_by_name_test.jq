if .data.allSchools.edges | length != 1 then
    "Expected 1 school" | halt_error(1)
elif .data.allSchools.edges[0].node.name != "Test School" then
    "Expected school to be named \"Test School\"" | halt_error(1)
else
    "PASS"
end
