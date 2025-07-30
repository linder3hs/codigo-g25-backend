import { Router } from "express";
import { ProductController } from "../controller/productController";
import { validateProduct } from "../middleware/validation";

const router = Router();

router.get("/", ProductController.getAllProduct);
router.get("/:id", ProductController.getProductById);
router.post("/", validateProduct, ProductController.createProduct);

export default router;
