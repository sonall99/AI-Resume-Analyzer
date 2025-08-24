import { motion } from "framer-motion";
import { useEffect } from "react";

export default function App() {
// Floating animation
const floatAnim = {
y: ["0%", "-5%", "0%"],
transition: { duration: 3, repeat: Infinity }
};

return (
<div className="w-full h-full font-sans text-white">
{/* Hero Section */}
<section className="h-screen bg-[#0a192f] flex flex-col justify-center items-center text-center">
<motion.h1
className="text-6xl font-bold tracking-wide"
animate={floatAnim}
>
Resume Analyzer
</motion.h1>
<motion.p
className="mt-6 text-xl text-gray-300"
initial={{ opacity: 0, y: 40 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 1.5 }}
>
AI-powered Resume Scoring & Suggestions
</motion.p>
<motion.a
href="#about"
className="mt-12 px-6 py-3 bg-blue-500 rounded-2xl shadow-lg hover:bg-blue-600 transition"
whileHover={{ scale: 1.05 }}
>
Learn More ↓
</motion.a>
</section>

{/* About Section */}  
  <section  
    id="about"  
    className="h-screen bg-white text-[#0a192f] flex flex-col justify-center items-center px-12"  
  >  
    <motion.h2  
      className="text-4xl font-bold mb-6"  
      initial={{ opacity: 0, y: 40 }}  
      whileInView={{ opacity: 1, y: 0 }}  
      transition={{ duration: 1 }}  
    >  
      About The Project  
    </motion.h2>  
    <motion.p  
      className="text-lg text-center max-w-2xl"  
      initial={{ opacity: 0 }}  
      whileInView={{ opacity: 1 }}  
      transition={{ duration: 1.5 }}  
    >  
      This project helps students and professionals evaluate their resumes  
      against job descriptions. It uses Machine Learning to score resumes  
      and Google Gemini AI to provide suggestions for improvements.  
    </motion.p>  
  </section>  

  {/* Features Section */}  
  <section className="h-screen bg-gradient-to-b from-blue-900 to-[#0a192f] flex flex-col justify-center items-center px-12">  
    <motion.h2  
      className="text-4xl font-bold mb-12"  
      initial={{ opacity: 0, y: 40 }}  
      whileInView={{ opacity: 1, y: 0 }}  
      transition={{ duration: 1 }}  
    >  
      Features  
    </motion.h2>  
    <div className="grid md:grid-cols-3 gap-8 max-w-5xl">  
      {[  
        { title: "Upload Resume", desc: "Upload your resume in PDF format." },  
        { title: "Get Score", desc: "Our ML model evaluates your resume." },  
        { title: "AI Suggestions", desc: "Gemini suggests improvements." }  
      ].map((feat, idx) => (  
        <motion.div  
          key={idx}  
          className="bg-white text-[#0a192f] p-8 rounded-2xl shadow-xl"  
          whileHover={{ scale: 1.05, rotate: 1 }}  
          initial={{ opacity: 0, y: 50 }}  
          whileInView={{ opacity: 1, y: 0 }}  
          transition={{ duration: 1, delay: idx * 0.3 }}  
        >  
          <h3 className="text-2xl font-bold mb-4">{feat.title}</h3>  
          <p className="text-gray-700">{feat.desc}</p>  
        </motion.div>  
      ))}  
    </div>  
  </section>  
</div>

);
}