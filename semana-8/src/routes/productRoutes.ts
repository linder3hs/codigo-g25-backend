import { Router } from "express";
import { ProductController } from "../controller/productController";
import { validateProduct } from "../middleware/validation";

const router = Router();

router.get("/", ProductController.getAllProduct);
router.get("/:id", ProductController.getProductById);
router.post("/", validateProduct, ProductController.createProduct);
router.put("/:id", ProductController.updateProduct);
router.delete("/:id", ProductController.deleteProduct);

export default router;
