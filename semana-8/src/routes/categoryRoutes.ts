import { Router } from "express";
import { CategoryController } from "../controller/categoryController";

const router = Router();

router.get("/", CategoryController.getAllCategories);

export default router;
