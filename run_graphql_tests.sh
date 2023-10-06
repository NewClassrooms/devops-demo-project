#! /bin/sh

# uses alpine's default shell, NOT bash.

for gql in *.graphql; do
    graphql_query=`jq -c -n --rawfile query "$gql" '{"query":$query}'`;
    test_file="$(basename "$gql" .graphql)_test.jq";
    curl -H "Content-Type: application/json" -X POST  -d "$graphql_query" $GRAPHQL_URL | jq -f "$test_file";
done
