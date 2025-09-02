"""
StudyAI AI Engine - Main Application Entry Point

Advanced AI processing service for educational content and agentic workflows.
"""

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import uvicorn
import os
import base64
from dotenv import load_dotenv

# Import our advanced AI services
from src.services.openai_service import EducationalAIService
from src.services.prompt_service import AdvancedPromptService

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="StudyAI AI Engine",
    description="Advanced AI processing for educational content and reasoning",
    version="2.0.0"
)

# Configure CORS for iOS app integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize AI services
ai_service = EducationalAIService()
prompt_service = AdvancedPromptService()

# Request/Response Models
class QuestionRequest(BaseModel):
    student_id: str
    question: str
    subject: str
    context: Optional[Dict] = None
    include_followups: Optional[bool] = True

class AdvancedReasoningResponse(BaseModel):
    answer: str
    reasoning_steps: List[str]
    key_concepts: List[str]
    follow_up_questions: List[str]
    difficulty_assessment: str
    learning_recommendations: List[str]

class LearningAnalysis(BaseModel):
    concepts_reinforced: List[str]
    difficulty_assessment: str
    next_recommendations: List[str]
    estimated_understanding: float
    subject_mastery_level: str

class AIEngineResponse(BaseModel):
    response: AdvancedReasoningResponse
    learning_analysis: LearningAnalysis
    processing_time_ms: int
    model_details: Dict[str, str]

class PracticeQuestionRequest(BaseModel):
    topic: str
    subject: str
    difficulty_level: Optional[str] = "medium"
    num_questions: Optional[int] = 3

class AnswerEvaluationRequest(BaseModel):
    question: str
    student_answer: str
    subject: str
    correct_answer: Optional[str] = None

class ImageAnalysisResponse(BaseModel):
    extracted_text: str
    mathematical_content: bool
    confidence_score: float
    processing_method: str
    suggestions: List[str]

# Health Check
@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "service": "StudyAI AI Engine",
        "version": "2.0.0",
        "features": ["advanced_prompting", "educational_optimization", "practice_generation"]
    }

# Main AI Processing Endpoint
@app.post("/api/v1/process-question", response_model=AIEngineResponse)
async def process_question(request: QuestionRequest):
    """
    Process educational questions with advanced AI reasoning and personalization.
    
    Features:
    - Subject-specific prompt optimization
    - Educational response formatting
    - Reasoning step extraction
    - Follow-up question generation
    - Learning analysis and recommendations
    """
    
    import time
    start_time = time.time()
    
    try:
        # Use our advanced AI service for processing
        result = await ai_service.process_educational_question(
            question=request.question,
            subject=request.subject,
            student_context=request.context,
            include_followups=request.include_followups
        )
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error", "AI processing failed"))
        
        # Calculate processing time
        processing_time = int((time.time() - start_time) * 1000)
        
        # Create advanced response
        advanced_response = AdvancedReasoningResponse(
            answer=result["answer"],
            reasoning_steps=result["reasoning_steps"],
            key_concepts=result["key_concepts"],
            follow_up_questions=result["follow_up_questions"],
            difficulty_assessment="appropriate_for_level",  # TODO: Implement difficulty analysis
            learning_recommendations=[
                f"Practice more problems involving {concept.lower()}" 
                for concept in result["key_concepts"][:2]
            ]
        )
        
        # Create learning analysis
        learning_analysis = LearningAnalysis(
            concepts_reinforced=result["key_concepts"],
            difficulty_assessment="appropriate_for_level",
            next_recommendations=[
                f"Explore advanced {request.subject} topics",
                "Try practice problems to reinforce understanding",
                "Review related concepts for deeper comprehension"
            ],
            estimated_understanding=0.85,  # TODO: Implement understanding estimation
            subject_mastery_level="developing"
        )
        
        return AIEngineResponse(
            response=advanced_response,
            learning_analysis=learning_analysis,
            processing_time_ms=processing_time,
            model_details={
                "model": "gpt-4o-mini",
                "prompt_optimization": "enabled",
                "educational_enhancement": "enabled",
                "subject_specialization": request.subject
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Engine processing error: {str(e)}")

# Practice Question Generation
@app.post("/api/v1/generate-practice")
async def generate_practice_questions(request: PracticeQuestionRequest):
    """Generate personalized practice questions for specific topics."""
    
    try:
        result = await ai_service.generate_practice_questions(
            topic=request.topic,
            subject=request.subject,
            difficulty_level=request.difficulty_level,
            num_questions=request.num_questions
        )
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error", "Practice generation failed"))
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Practice generation error: {str(e)}")

# Answer Evaluation
@app.post("/api/v1/evaluate-answer")
async def evaluate_student_answer(request: AnswerEvaluationRequest):
    """Evaluate student's work and provide constructive feedback."""
    
    try:
        result = await ai_service.evaluate_student_answer(
            question=request.question,
            student_answer=request.student_answer,
            subject=request.subject,
            correct_answer=request.correct_answer
        )
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error", "Answer evaluation failed"))
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Answer evaluation error: {str(e)}")

# Subject Analysis
@app.get("/api/v1/subjects")
async def get_supported_subjects():
    """Get list of supported subjects with their capabilities."""
    return {
        "subjects": [
            {
                "name": "Mathematics",
                "code": "mathematics", 
                "features": ["step_by_step_solutions", "equation_formatting", "concept_explanation"],
                "specializations": ["algebra", "geometry", "calculus", "statistics"]
            },
            {
                "name": "Physics",
                "code": "physics",
                "features": ["unit_analysis", "formula_derivation", "concept_visualization"],
                "specializations": ["mechanics", "thermodynamics", "electromagnetism", "quantum"]
            },
            {
                "name": "Chemistry", 
                "code": "chemistry",
                "features": ["equation_balancing", "molecular_structure", "reaction_mechanisms"],
                "specializations": ["organic", "inorganic", "physical", "analytical"]
            },
            {
                "name": "Biology",
                "code": "biology", 
                "features": ["process_explanation", "system_analysis", "concept_connections"],
                "specializations": ["cell_biology", "genetics", "ecology", "anatomy"]
            }
        ]
    }

# Personalization Profile
@app.get("/api/v1/personalization/{student_id}")
async def get_personalization_profile(student_id: str):
    """Get personalized learning profile for student."""
    # TODO: Implement actual personalization profile retrieval
    return {
        "student_id": student_id, 
        "learning_level": "high_school",
        "strong_subjects": ["mathematics", "physics"],
        "areas_for_improvement": ["chemistry", "biology"],
        "preferred_explanation_style": "step_by_step",
        "recent_topics": ["quadratic_equations", "force_analysis"]
    }

# Image Upload and Analysis Endpoint
@app.post("/api/v1/analyze-image", response_model=ImageAnalysisResponse)
async def analyze_image_content(
    image: UploadFile = File(...),
    subject: Optional[str] = Form("general"),
    student_id: Optional[str] = Form("anonymous")
):
    """
    Upload and analyze image content for mathematical and educational content extraction.
    
    This endpoint uses OpenAI's Vision API to process images containing:
    - Complex mathematical equations and formulas
    - Handwritten mathematical content
    - Diagrams, graphs, and charts
    - Scientific notation and symbols
    - Mixed text and mathematical content
    
    Args:
        image: Image file (JPEG, PNG, WebP)
        subject: Academic subject context for better analysis
        student_id: Student identifier for personalization
        
    Returns:
        Extracted content with mathematical formatting and analysis suggestions
    """
    
    import time
    start_time = time.time()
    
    try:
        # Validate file type
        if not image.content_type or not image.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Validate file size (max 5MB for API cost management)
        contents = await image.read()
        if len(contents) > 5 * 1024 * 1024:  # 5MB limit
            raise HTTPException(status_code=400, detail="Image file too large (max 5MB)")
        
        # Convert to base64 for OpenAI API
        base64_image = base64.b64encode(contents).decode('utf-8')
        
        # Use AI service to process the image
        result = await ai_service.analyze_image_content(
            base64_image=base64_image,
            image_format=image.content_type.split('/')[-1],
            subject=subject,
            student_context={"student_id": student_id}
        )
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error", "Image analysis failed"))
        
        # Calculate processing time
        processing_time = int((time.time() - start_time) * 1000)
        
        return ImageAnalysisResponse(
            extracted_text=result["extracted_text"],
            mathematical_content=result["has_math"],
            confidence_score=result["confidence"],
            processing_method="openai_vision_gpt4o",
            suggestions=result["suggestions"]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image analysis error: {str(e)}")

# Process Image with Question Context
@app.post("/api/v1/process-image-question")
async def process_image_with_question(
    image: UploadFile = File(...),
    question: Optional[str] = Form(""),
    subject: str = Form("general"),
    student_id: Optional[str] = Form("anonymous")
):
    """
    Process an image with optional question context for comprehensive analysis.
    
    This combines image analysis with question processing to provide:
    - Extracted mathematical content from the image
    - AI-powered explanation and solution steps
    - Subject-specific educational guidance
    - Follow-up questions and learning recommendations
    """
    
    import time
    start_time = time.time()
    
    try:
        # Validate and process image (same validation as analyze-image)
        if not image.content_type or not image.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        contents = await image.read()
        if len(contents) > 5 * 1024 * 1024:  # 5MB limit
            raise HTTPException(status_code=400, detail="Image file too large (max 5MB)")
        
        base64_image = base64.b64encode(contents).decode('utf-8')
        
        # Process image with question context
        result = await ai_service.process_image_with_question(
            base64_image=base64_image,
            image_format=image.content_type.split('/')[-1],
            question=question,
            subject=subject,
            student_context={"student_id": student_id}
        )
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result.get("error", "Image processing failed"))
        
        # Calculate processing time
        processing_time = int((time.time() - start_time) * 1000)
        
        # Create comprehensive response combining image analysis and question processing
        advanced_response = AdvancedReasoningResponse(
            answer=result["answer"],
            reasoning_steps=result["reasoning_steps"],
            key_concepts=result["key_concepts"],
            follow_up_questions=result["follow_up_questions"],
            difficulty_assessment="extracted_from_image",
            learning_recommendations=result["learning_recommendations"]
        )
        
        learning_analysis = LearningAnalysis(
            concepts_reinforced=result["key_concepts"],
            difficulty_assessment="image_based_analysis",
            next_recommendations=result["next_steps"],
            estimated_understanding=result.get("confidence", 0.85),
            subject_mastery_level="analysis_required"
        )
        
        return {
            "response": advanced_response,
            "learning_analysis": learning_analysis,
            "image_analysis": {
                "extracted_content": result["extracted_text"],
                "mathematical_content": result["has_math"],
                "processing_method": "openai_vision_gpt4o"
            },
            "processing_time_ms": processing_time,
            "model_details": {
                "model": "gpt-4o",
                "vision_enabled": True,
                "prompt_optimization": "enabled",
                "image_analysis": "enabled"
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image processing error: {str(e)}")

if __name__ == "__main__":
    # Get port from environment variable (Railway sets this automatically)
    port_env = os.getenv("PORT", "8000")
    print(f"🔍 DEBUG: Raw PORT environment variable: '{port_env}'")
    print(f"🔍 DEBUG: PORT type: {type(port_env)}")
    
    try:
        port = int(port_env)
        print(f"✅ DEBUG: Successfully parsed PORT: {port}")
    except ValueError as e:
        print(f"❌ DEBUG: Failed to parse PORT '{port_env}': {e}")
        print("🔄 DEBUG: Using default port 8000")
        port = 8000
    
    print(f"🚀 DEBUG: Starting server on 0.0.0.0:{port}")
    
    # Production server
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        log_level="info"
    )