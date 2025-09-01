"""
OpenAI Service with Advanced Educational Processing

Handles OpenAI API integration with sophisticated prompt engineering
and educational response optimization.
"""

import openai
import asyncio
from typing import Dict, List, Optional, Any
from .prompt_service import AdvancedPromptService, Subject
import os
from dotenv import load_dotenv

load_dotenv()


class EducationalAIService:
    """
    Advanced AI service specifically designed for educational content processing.
    Uses sophisticated prompt engineering and response optimization.
    """
    
    def __init__(self):
        self.client = openai.AsyncOpenAI(
            api_key=os.getenv('OPENAI_API_KEY')
        )
        self.prompt_service = AdvancedPromptService()
        self.model = "gpt-4o-mini"  # or "gpt-4" for more complex tasks
    
    async def process_educational_question(
        self, 
        question: str, 
        subject: str,
        student_context: Optional[Dict] = None,
        include_followups: bool = True
    ) -> Dict[str, Any]:
        """
        Process an educational question with advanced AI reasoning.
        
        Args:
            question: Student's question
            subject: Academic subject
            student_context: Optional context about the student's learning profile
            include_followups: Whether to generate follow-up questions
            
        Returns:
            Comprehensive response with explanation, steps, and follow-ups
        """
        
        try:
            # Create enhanced prompt using our prompt engineering service
            system_prompt = self.prompt_service.create_enhanced_prompt(
                question=question,
                subject_string=subject,
                context=student_context
            )
            
            # Call OpenAI with optimized prompt
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                temperature=0.3,  # Lower temperature for more consistent educational content
                max_tokens=1500,
                presence_penalty=0.1,
                frequency_penalty=0.1
            )
            
            raw_answer = response.choices[0].message.content
            
            # Optimize the response for better formatting
            optimized_answer = self.prompt_service.optimize_response(raw_answer, subject)
            
            # Generate follow-up questions if requested
            follow_ups = []
            if include_followups:
                follow_ups = self.prompt_service.generate_follow_up_questions(question, subject)
            
            # Extract reasoning steps if present
            reasoning_steps = self._extract_reasoning_steps(optimized_answer)
            
            # Identify key concepts covered
            concepts = self._identify_key_concepts(optimized_answer, subject)
            
            return {
                "success": True,
                "answer": optimized_answer,
                "reasoning_steps": reasoning_steps,
                "key_concepts": concepts,
                "follow_up_questions": follow_ups,
                "subject": subject,
                "processing_details": {
                    "model_used": self.model,
                    "prompt_optimization": True,
                    "response_optimization": True,
                    "educational_enhancement": True
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "answer": "I apologize, but I encountered an error processing your question. Please try again.",
                "reasoning_steps": [],
                "key_concepts": [],
                "follow_up_questions": []
            }
    
    def _extract_reasoning_steps(self, response: str) -> List[str]:
        """Extract step-by-step reasoning from the AI response."""
        steps = []
        lines = response.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for numbered steps or step indicators
            if (line.startswith(('Step ', 'step ', '1.', '2.', '3.', '4.', '5.')) or
                'Step' in line and ':' in line):
                steps.append(line)
        
        return steps
    
    def _identify_key_concepts(self, response: str, subject: str) -> List[str]:
        """Identify key educational concepts mentioned in the response."""
        concepts = []
        response_lower = response.lower()
        
        # Subject-specific concept identification
        math_concepts = [
            'equation', 'fraction', 'algebra', 'geometry', 'calculus',
            'derivative', 'integral', 'function', 'variable', 'coefficient',
            'exponent', 'logarithm', 'trigonometry', 'polynomial'
        ]
        
        physics_concepts = [
            'velocity', 'acceleration', 'force', 'energy', 'momentum',
            'gravity', 'friction', 'wave', 'frequency', 'amplitude',
            'electric', 'magnetic', 'thermodynamics', 'quantum'
        ]
        
        chemistry_concepts = [
            'molecule', 'atom', 'bond', 'reaction', 'catalyst',
            'oxidation', 'reduction', 'acid', 'base', 'solution',
            'concentration', 'equilibrium', 'organic', 'inorganic'
        ]
        
        concept_lists = {
            'mathematics': math_concepts,
            'physics': physics_concepts,
            'chemistry': chemistry_concepts
        }
        
        # Get relevant concepts for the subject
        relevant_concepts = concept_lists.get(subject.lower(), [])
        
        for concept in relevant_concepts:
            if concept in response_lower:
                concepts.append(concept.title())
        
        return list(set(concepts))  # Remove duplicates
    
    async def generate_practice_questions(
        self, 
        topic: str, 
        subject: str, 
        difficulty_level: str = "medium",
        num_questions: int = 3
    ) -> Dict[str, Any]:
        """
        Generate practice questions for a specific topic.
        This is perfect for future features like personalized practice.
        """
        
        try:
            system_prompt = f"""You are an expert educational content creator. Generate {num_questions} practice questions for the topic "{topic}" in {subject}.

Requirements:
- Difficulty level: {difficulty_level}
- Questions should build upon each other in complexity
- Include clear, step-by-step solutions
- Use mobile-friendly mathematical notation
- Focus on understanding, not just computation

Format each question as:
Question N: [question text]
Solution: [detailed solution with steps]
Key Concept: [main concept being tested]
"""
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Generate practice questions for: {topic}"}
                ],
                temperature=0.5,  # Slightly higher for variety in questions
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            questions = self._parse_generated_questions(content)
            
            return {
                "success": True,
                "topic": topic,
                "subject": subject,
                "difficulty_level": difficulty_level,
                "questions": questions
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "questions": []
            }
    
    def _parse_generated_questions(self, content: str) -> List[Dict[str, str]]:
        """Parse generated questions into structured format."""
        questions = []
        current_question = {}
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            
            if line.startswith('Question'):
                if current_question:
                    questions.append(current_question)
                current_question = {"question": line}
            elif line.startswith('Solution:'):
                current_question["solution"] = line[9:].strip()
            elif line.startswith('Key Concept:'):
                current_question["key_concept"] = line[12:].strip()
        
        if current_question:
            questions.append(current_question)
        
        return questions
    
    async def evaluate_student_answer(
        self,
        question: str,
        student_answer: str,
        subject: str,
        correct_answer: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Evaluate a student's answer and provide constructive feedback.
        Perfect for future assessment features.
        """
        
        try:
            system_prompt = f"""You are an expert {subject} tutor. Evaluate the student's answer and provide constructive feedback.

Focus on:
1. Correctness of the final answer
2. Quality of the reasoning process
3. Common mistakes or misconceptions
4. Suggestions for improvement
5. Encouragement and positive reinforcement

Be supportive and educational in your feedback."""
            
            user_message = f"""Question: {question}

Student's Answer: {student_answer}

{f"Correct Answer: {correct_answer}" if correct_answer else ""}

Please evaluate this answer and provide helpful feedback."""
            
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            feedback = response.choices[0].message.content
            
            return {
                "success": True,
                "feedback": feedback,
                "subject": subject
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "feedback": "Unable to evaluate answer at this time."
            }