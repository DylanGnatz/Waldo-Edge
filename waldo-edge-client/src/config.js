export default {
  s3: {
    REGION: "us-west-2",
    BUCKET: "people-finder-photos"
  },
  apiGateway: {
    REGION: "us-west-2",
    URL: "https://8hkmemu2ld.execute-api.us-west-2.amazonaws.com/prod"
  },
  cognito: {
    REGION: "us-west-2",
    USER_POOL_ID: "us-west-2_HDqJr1yiX",
    APP_CLIENT_ID: "48bq37oeegc5m8lucl94n1psed",
    IDENTITY_POOL_ID: "us-west-2:9d3ef920-cc12-4eb9-b555-79a7e0e0aef7"
  }
};
