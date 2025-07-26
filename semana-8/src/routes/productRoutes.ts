import { Router } from "express";
import { ProductController } from "../controller/productController";

const router = Router();

router.get("/", ProductController.getAllProduct);
router.post("/", ProductController.createProduct);

export default router;
