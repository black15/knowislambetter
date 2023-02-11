import { GraphQLClient, gql } from "graphql-request";

const graphql_django = process.env.DJANGO_GRAPHQL_API

// const client = new GraphQLClient(graphql_django)

interface Tag {
   id: string | number,
   name: string
}
interface Author {
   firstName: string,
   lastName: string,
   username: string,
   email: string,
}
interface Post{
   id: string | number,
   title: string,
   slug: string,
   body: string,
   published: boolean,
   createdAt: string,
   updatedAt: string,
   author: Author[],
   tags: Tag[]
}

const ALL_POSTS_IDS = gql`
   query {
      posts {
         id
      }
   }
`

const ALL_POSTS = gql`
   query {
      posts {
         id
         title
         slug
         body
         published
         createdAt
         updatedAt
         author {
           firstName
           lastName
           username
           email
         }
         tags {
           name
         }
      }
   }
`

const POST_QUERY = gql`
   query($slug: String!) {
      postBySlug(slug: $slug){
         id
         title
         slug
         body
         published
         createdAt
         updatedAt
         author {
           firstName
           lastName
           username
           email
         }
         tags {
           name
         }
      }
   }
`