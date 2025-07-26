import { Router } from "express";
import { ProductController } from "../controller/productController";
import { validateProduct } from "../middleware/validation";

const router = Router();

router.get("/", ProductController.getAllProduct);
router.post("/", validateProduct, ProductController.createProduct);

export default router;
