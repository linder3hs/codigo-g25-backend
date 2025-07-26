import express from "express";

const app = express();

app.get("/", (request, response) => {
  response.json({
    message: "Hola mundo",
  });
});

app.listen(3000, () => {
  console.log("El servidor inicio.");
});
