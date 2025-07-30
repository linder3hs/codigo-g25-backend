import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import { connectDB } from "./config/database";
import { categoryRouter, productRouter } from "./routes";
import { errorHandler, notFound } from "./middleware/errorHandler";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// permitir que el navegador puede hacer peticiones
app.use(cors());
// esto permite leer el body de las peticiones
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

connectDB();

app.get("/", (request, response) => {
  response.json({
    message: "Hola mundo",
  });
});

app.use("/api/v1/products", productRouter);
app.use("/api/v1/categories", categoryRouter);

app.use(errorHandler);
app.use(notFound);

app.listen(3000, () => {
  console.log("El servidor inicio.");
});
