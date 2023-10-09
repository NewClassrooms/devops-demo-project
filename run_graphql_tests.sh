#! /bin/sh

# uses alpine's default shell, NOT bash.
cd graphql_tests
shopt -s nullglob
for gql in *.graphql; do
    graphql_query=`jq -c -n --rawfile query "$gql" '{"query":$query}'`;
    test_file="$(basename "$gql" .graphql)_test.jq";
    echo "${test_file}";
    curl -sS -H "Content-Type: application/json" -X POST  -d "$graphql_query" $GRAPHQL_URL | jq -f "$test_file" || break;
    echo;
done
shopt -u nullglob
echo;
