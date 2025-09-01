"""
Advanced Prompt Engineering Service for StudyAI AI Engine

Handles sophisticated educational prompting, subject-specific optimization,
and intelligent response formatting for different academic domains.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
import re


class Subject(Enum):
    MATHEMATICS = "mathematics"
    PHYSICS = "physics" 
    CHEMISTRY = "chemistry"
    BIOLOGY = "biology"
    HISTORY = "history"
    LITERATURE = "literature"
    COMPUTER_SCIENCE = "computer_science"
    ECONOMICS = "economics"
    GENERAL = "general"


class PromptTemplate:
    def __init__(self, subject: Subject, base_prompt: str, formatting_rules: List[str], examples: List[str]):
        self.subject = subject
        self.base_prompt = base_prompt
        self.formatting_rules = formatting_rules
        self.examples = examples


class AdvancedPromptService:
    """
    Advanced prompt engineering service for educational AI processing.
    Handles subject-specific prompting, formatting optimization, and response enhancement.
    """
    
    def __init__(self):
        self.prompt_templates = self._initialize_prompt_templates()
        self.math_subjects = {Subject.MATHEMATICS, Subject.PHYSICS, Subject.CHEMISTRY}
    
    def _initialize_prompt_templates(self) -> Dict[Subject, PromptTemplate]:
        """Initialize specialized prompt templates for different subjects."""
        
        templates = {}
        
        # Mathematics Template
        templates[Subject.MATHEMATICS] = PromptTemplate(
            subject=Subject.MATHEMATICS,
            base_prompt="""You are an expert mathematics tutor providing educational content for iOS mobile devices. Your responses will be rendered using MathJax on iPhone/iPad screens with limited vertical space.""",
            formatting_rules=[
                "🚨 CRITICAL iOS MOBILE MATH RENDERING RULES:",
                "",
                "📱 MOBILE SCREEN OPTIMIZATION:",
                "Your math will be displayed on iPhone/iPad screens - choose formatting carefully!",
                "",
                "1. SINGLE EXPRESSION RULE - Never nest $ delimiters:",
                "   ✅ CORRECT: '$0 < |x - c| < \\delta \\implies |f(x) - L| < \\epsilon$'",
                "   ❌ WRONG: '$0 < |x - c| < $\\delta$ \\implies |f(x) - L| < \\epsilon$'",
                "   ❌ WRONG: 'For every $\\epsilon > 0$, there exists $\\delta > 0$'",
                "",
                "2. MOBILE DISPLAY MATH - Use $$ for tall expressions that need vertical space:",
                "   ✅ Use $$...$$ for: limits, integrals, large fractions, summations",
                "   ✅ Use $...$ for: simple variables, short expressions",
                "",
                "   EXAMPLES - When to use display math ($$):",
                "   ✅ $$\\lim_{x \\to c} f(x) = L$$ (subscripts need space)",
                "   ✅ $$\\int_a^b f(x) dx$$ (limits need space)", 
                "   ✅ $$\\sum_{i=1}^n x_i$$ (summation bounds need space)",
                "   ✅ $$\\frac{\\sqrt{b^2-4ac}}{2a}$$ (complex fraction needs space)",
                "   ✅ $$x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$$ (quadratic formula)",
                "",
                "   EXAMPLES - When to use inline math ($):",
                "   ✅ $f(x) = 2x + 3$ (simple function)",
                "   ✅ $\\epsilon > 0$ (simple inequality)", 
                "   ✅ $x \\in \\mathbb{R}$ (set membership)",
                "   ✅ $\\sin(x)$ (simple function)",
                "",
                "3. Greek letters - ALWAYS use LaTeX commands in $ delimiters:",
                "   ✅ $\\alpha$, $\\beta$, $\\gamma$, $\\delta$, $\\epsilon$, $\\theta$, $\\phi$, $\\psi$, $\\omega$",
                "   ❌ Never use: α, β, γ, δ, ε, θ, φ, ψ, ω (raw Unicode)",
                "",
                "4. Mathematical operators - ALWAYS in $ delimiters:",
                "   ✅ $\\leq$, $\\geq$, $\\neq$, $\\approx$, $\\equiv$, $\\cdot$, $\\times$, $\\pm$",
                "   ❌ Never use: ≤, ≥, ≠, ≈, ≡, ·, ×, ± (raw Unicode)",
                "",
                "5. MOBILE-SPECIFIC FORMATTING:",
                "   • Break long expressions into multiple lines",
                "   • Use display math for expressions with vertical elements",
                "   • Keep inline math simple and short",
                "   • Test: 'Would this render clearly on an iPhone screen?'",
                "",
                "6. QUALITY CHECK for iOS rendering:",
                "   • No nested $ delimiters (breaks MathJax)",
                "   • Tall expressions use $$ (prevents clipping)",
                "   • All Greek letters wrapped: $\\epsilon$, not ε", 
                "   • All operators wrapped: $\\leq$, not ≤",
                "   • Complex expressions get their own display block"
            ],
            examples=[
                "PERFECT iOS MOBILE MATH FORMATTING:",
                "",
                "EPSILON-DELTA DEFINITION (mobile optimized):",
                "The epsilon-delta definition provides a rigorous way to define limits.",
                "",
                "We say that:",
                "$$\\lim_{x \\to c} f(x) = L$$",
                "",
                "This means for every $\\epsilon > 0$, there exists $\\delta > 0$ such that:",
                "$$0 < |x - c| < \\delta \\implies |f(x) - L| < \\epsilon$$",
                "",
                "Breaking this down:",
                "- $\\epsilon$ represents our tolerance for how close $f(x)$ must be to $L$",
                "- $\\delta$ represents how close $x$ must be to $c$", 
                "- The implication shows the relationship between these distances",
                "",
                "DIFFERENTIAL PRIVACY EXAMPLE (mobile optimized):",
                "A mechanism $M$ satisfies $\\epsilon$-differential privacy if:",
                "$$P(M(D) \\in S) \\leq e^{\\epsilon} \\cdot P(M(D') \\in S)$$",
                "",  
                "Key points:",
                "- $D$ and $D'$ are datasets differing by one record",
                "- $\\epsilon$ controls the privacy parameter",
                "- $e^{\\epsilon}$ bounds the privacy loss ratio"
            ]
        )
        
        # Physics Template
        templates[Subject.PHYSICS] = PromptTemplate(
            subject=Subject.PHYSICS,
            base_prompt="""You are an expert physics tutor. Explain physics concepts clearly with real-world applications, proper units, and step-by-step problem solving.""",
            formatting_rules=[
                "Always include proper units (m/s, N, J, etc.)",
                "Use clear variable definitions",
                "Show formula first, then substitution",
                "Explain the physics concept behind each step",
                "Use simple mathematical notation for mobile display",
                "Include diagrams descriptions when helpful"
            ],
            examples=[
                "Given: v₀ = 10 m/s, a = 5 m/s², t = 3 s",
                "Formula: v = v₀ + at",
                "Substitution: v = 10 + (5)(3) = 25 m/s"
            ]
        )
        
        # Chemistry Template  
        templates[Subject.CHEMISTRY] = PromptTemplate(
            subject=Subject.CHEMISTRY,
            base_prompt="""You are an expert chemistry tutor. Provide clear explanations of chemical concepts, balanced equations, and step-by-step problem solving with proper chemical notation.""",
            formatting_rules=[
                "Use simple chemical formulas: H2O, CO2, etc.",
                "Show balanced chemical equations clearly",
                "Include proper units for measurements", 
                "Explain chemical concepts and reasoning",
                "Use clear step-by-step approach for calculations",
                "Define chemical terms when first used"
            ],
            examples=[
                "Balanced equation: 2H2 + O2 → 2H2O",
                "Molar ratio: 2 mol H2 : 1 mol O2 : 2 mol H2O"
            ]
        )
        
        # Add more subjects as needed...
        templates[Subject.GENERAL] = PromptTemplate(
            subject=Subject.GENERAL,
            base_prompt="""You are an expert tutor. Provide clear, educational explanations that help students understand concepts step-by-step.""",
            formatting_rules=[
                "Use clear, structured explanations",
                "Break complex topics into simple steps", 
                "Provide examples when helpful",
                "Use proper formatting for mobile display"
            ],
            examples=[]
        )
        
        return templates
    
    def detect_subject(self, subject_string: str) -> Subject:
        """Detect the academic subject from a string."""
        subject_lower = subject_string.lower()
        
        subject_mapping = {
            'math': Subject.MATHEMATICS,
            'mathematics': Subject.MATHEMATICS,
            'algebra': Subject.MATHEMATICS,
            'geometry': Subject.MATHEMATICS,
            'calculus': Subject.MATHEMATICS,
            'statistics': Subject.MATHEMATICS,
            'physics': Subject.PHYSICS,
            'chemistry': Subject.CHEMISTRY,
            'biology': Subject.BIOLOGY,
            'history': Subject.HISTORY,
            'literature': Subject.LITERATURE,
            'computer': Subject.COMPUTER_SCIENCE,
            'programming': Subject.COMPUTER_SCIENCE,
            'economics': Subject.ECONOMICS,
        }
        
        for key, subject in subject_mapping.items():
            if key in subject_lower:
                return subject
                
        return Subject.GENERAL
    
    def create_enhanced_prompt(self, question: str, subject_string: str, context: Optional[Dict] = None) -> str:
        """
        Create an enhanced prompt with subject-specific optimization.
        
        Args:
            question: The student's question
            subject_string: Subject area (e.g., 'mathematics', 'physics')
            context: Optional context like student level, learning history
            
        Returns:
            Enhanced prompt optimized for the specific subject and context
        """
        subject = self.detect_subject(subject_string)
        template = self.prompt_templates.get(subject, self.prompt_templates[Subject.GENERAL])
        
        # Build the enhanced system prompt
        system_prompt_parts = [
            template.base_prompt,
            "",
            "IMPORTANT FORMATTING GUIDELINES:",
        ]
        
        # Add formatting rules
        for i, rule in enumerate(template.formatting_rules, 1):
            system_prompt_parts.append(f"{i}. {rule}")
        
        # Add examples if available
        if template.examples:
            system_prompt_parts.extend([
                "",
                "EXAMPLE OF GOOD FORMATTING:",
                *template.examples
            ])
        
        # Add context-specific instructions
        if context:
            system_prompt_parts.extend([
                "",
                "STUDENT CONTEXT:",
                self._format_context_instructions(context)
            ])
        
        # Add subject-specific enhancements
        if subject in self.math_subjects:
            system_prompt_parts.extend([
                "",
                "MATHEMATICAL FORMATTING REQUIREMENTS:",
                "- ALL mathematical expressions MUST use LaTeX notation",
                "- Inline math: $expression$ (single dollar signs)",
                "- Display math: $$expression$$ (double dollar signs)",
                "- NO markdown headers (###), bold (**), or bullet points (-)",
                "- NO plain text math notation like 'x^2' or '3/4'",
                "- Use \\frac{}{}, \\sqrt{}, x^{} consistently",
                "- Write complete sentences between mathematical expressions",
                "- Separate solution steps with blank lines for clarity"
            ])
        
        system_prompt_parts.extend([
            "",
            "Remember: Your goal is to help the student LEARN and UNDERSTAND, not just get the right answer."
        ])
        
        return "\n".join(system_prompt_parts)
    
    def _format_context_instructions(self, context: Dict) -> str:
        """Format context information into instruction text."""
        instructions = []
        
        if 'learning_level' in context:
            level = context['learning_level']
            instructions.append(f"- Adjust explanation complexity for {level} level")
        
        if 'weak_areas' in context and context['weak_areas']:
            weak_areas = ", ".join(context['weak_areas'])
            instructions.append(f"- Pay special attention to: {weak_areas}")
        
        if 'learning_style' in context:
            style = context['learning_style']
            instructions.append(f"- Adapt to {style} learning style")
            
        return "\n".join(instructions) if instructions else "- Provide comprehensive, clear explanations"
    
    def optimize_response(self, response: str, subject_string: str) -> str:
        """
        Post-process AI response for better formatting and clarity.
        
        Args:
            response: Raw AI response
            subject_string: Subject area for context
            
        Returns:
            Optimized response with better formatting
        """
        subject = self.detect_subject(subject_string)
        optimized = response
        
        # Apply subject-specific optimizations
        if subject in self.math_subjects:
            optimized = self._optimize_math_response(optimized)
        
        # General optimizations
        optimized = self._apply_general_optimizations(optimized)
        
        return optimized
    
    def _optimize_math_response(self, response: str) -> str:
        """Optimize mathematical content in responses."""
        optimized = response
        
        # Remove markdown formatting that shouldn't be in math responses
        optimized = re.sub(r'^### .+$', r'', optimized, flags=re.MULTILINE)  # Remove ### headers
        optimized = re.sub(r'\*\*(.+?)\*\*', r'\1', optimized)  # Remove ** bold formatting
        optimized = re.sub(r'^- ', r'', optimized, flags=re.MULTILINE)  # Remove bullet points
        optimized = re.sub(r'^\d+\. ', r'', optimized, flags=re.MULTILINE)  # Remove numbered lists
        
        # Fix stray LaTeX expressions that aren't wrapped in $ delimiters
        def fix_stray_latex(text):
            # More comprehensive LaTeX command detection
            patterns_to_fix = [
                # Greek letters
                (r'(?<!\$)\\(epsilon|delta|alpha|beta|gamma|theta|phi|psi|omega|sigma|lambda|mu|nu|xi|rho|tau|chi)(?!\$)', r'$\\\1$'),
                # Math operators and symbols  
                (r'(?<!\$)\\(leq|geq|neq|approx|equiv|cdot|times|div|pm|mp|cap|cup|subset|supset|in|notin|infty)(?!\$)', r'$\\\1$'),
                # Functions with arguments
                (r'(?<!\$)\\(sqrt|frac|sum|int|log|ln|sin|cos|tan|sec|csc|cot)\{[^}]*\}(?!\{[^}]*\})*(?!\$)', r'$\g<0>$'),
                # Simple expressions like "< ε" or "> ε"  
                (r'([<>=])\s*([εδαβγθφψωσλμνξρτχ])', r'\1 $\2$'),
                # Standalone Greek letters in text
                (r'(?<![a-zA-Z$])([εδαβγθφψωσλμνξρτχ])(?![a-zA-Z$])', r'$\1$'),
            ]
            
            for pattern, replacement in patterns_to_fix:
                text = re.sub(pattern, replacement, text)
            
            return text
        
        # Fix nested dollar signs (critical iOS rendering issue)
        def fix_nested_dollars(text):
            # Pattern: $...some content...$variable$...more content...$
            # This creates double $$ around variable which breaks MathJax
            
            # Find patterns like: $0 < |x - c| < $\delta$ \implies |f(x) - L| < \epsilon$
            # Should become: $0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$
            
            # Method: Remove inner $ delimiters within existing $ expressions
            def fix_inner_dollars(match):
                full_expr = match.group(0)  # The entire $...$ expression
                # Remove any $ that appear inside this expression (except the outer ones)
                inner_content = full_expr[1:-1]  # Remove outer $
                # Remove any remaining $ signs from inner content
                cleaned_inner = inner_content.replace('$', '')
                return f'${cleaned_inner}$'
            
            # Find complete math expressions and clean inner dollars
            # This regex finds $...$ expressions that may contain inner $
            text = re.sub(r'\$[^$]*\$[^$]*\$[^$]*\$', fix_inner_dollars, text)
            
            # Also handle simpler cases: $...$variable$...$
            text = re.sub(r'\$([^$]*)\$([^$\s]+)\$([^$]*)\$', r'$\1\2\3$', text)
            
            return text
        
        optimized = fix_stray_latex(optimized)
        optimized = fix_nested_dollars(optimized)
        
        # Ensure proper spacing around operators (but preserve LaTeX)
        # Only apply to non-LaTeX content (outside of $ delimiters)
        def fix_spacing_outside_latex(text):
            parts = re.split(r'(\$.*?\$)', text)
            for i in range(0, len(parts), 2):  # Process non-LaTeX parts
                if parts[i]:
                    parts[i] = re.sub(r'([a-zA-Z0-9])=([a-zA-Z0-9])', r'\1 = \2', parts[i])
                    parts[i] = re.sub(r'([0-9])\+([0-9])', r'\1 + \2', parts[i])
                    parts[i] = re.sub(r'([0-9])-([0-9])', r'\1 - \2', parts[i])
            return ''.join(parts)
        
        optimized = fix_spacing_outside_latex(optimized)
        
        # Clean up multiple spaces and empty lines
        optimized = re.sub(r' +', ' ', optimized)
        optimized = re.sub(r'\n\s*\n\s*\n', '\n\n', optimized)  # Max 2 consecutive newlines
        
        return optimized.strip()
    
    def _apply_general_optimizations(self, response: str) -> str:
        """Apply general formatting optimizations."""
        lines = response.split('\n')
        optimized_lines = []
        
        for line in lines:
            # Clean up whitespace
            line = line.strip()
            if line:
                optimized_lines.append(line)
            
        return '\n'.join(optimized_lines)
    
    def generate_follow_up_questions(self, original_question: str, subject_string: str) -> List[str]:
        """
        Generate intelligent follow-up questions based on the original question.
        This helps students explore related concepts and deepen understanding.
        """
        subject = self.detect_subject(subject_string)
        
        if subject == Subject.MATHEMATICS:
            return self._generate_math_followups(original_question)
        elif subject == Subject.PHYSICS:
            return self._generate_physics_followups(original_question)
        elif subject == Subject.CHEMISTRY:
            return self._generate_chemistry_followups(original_question)
        else:
            return self._generate_general_followups(original_question)
    
    def _generate_math_followups(self, question: str) -> List[str]:
        """Generate math-specific follow-up questions."""
        followups = []
        
        if 'solve' in question.lower() and '=' in question:
            followups.extend([
                "Can you verify this answer by substituting back into the original equation?",
                "What would happen if we changed one of the coefficients?",
                "Can you solve a similar equation with different numbers?"
            ])
        
        if any(term in question.lower() for term in ['fraction', '/', 'divide']):
            followups.extend([
                "Can you convert this to a decimal?",
                "What would this fraction look like as a percentage?",
                "Can you simplify this fraction further?"
            ])
            
        return followups[:3]  # Limit to 3 follow-ups
    
    def _generate_physics_followups(self, question: str) -> List[str]:
        """Generate physics-specific follow-up questions."""
        return [
            "What real-world applications does this concept have?",
            "How would changing the initial conditions affect the result?",
            "What assumptions did we make in solving this problem?"
        ]
    
    def _generate_chemistry_followups(self, question: str) -> List[str]:
        """Generate chemistry-specific follow-up questions.""" 
        return [
            "What would happen if we used different reactants?",
            "How does temperature affect this reaction?",
            "What are the safety considerations for this process?"
        ]
    
    def _generate_general_followups(self, question: str) -> List[str]:
        """Generate general follow-up questions."""
        return [
            "Can you think of examples of this concept in everyday life?",
            "What questions do you still have about this topic?",
            "How does this relate to what you've learned before?"
        ]