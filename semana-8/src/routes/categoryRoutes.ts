import { Router } from "express";
import { CategoryController } from "../controller/categoryController";

const router = Router();

router.get("/", CategoryController.getAllCategories);
router.post("/", CategoryController.createCategory);

export default router;
