---
theme: seriph
layout: center
background: 'https://images.unsplash.com/photo-1519003722824-194d4455a60c?auto=format&fit=crop&w=1920&q=80'
---

<div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-white">
  <h1 class="custom-title mb-10 animate-fade-in">感谢聆听</h1>
  <div class="w-64 h-1 bg-gradient-to-r from-blue-400 to-purple-500 mx-auto rounded-full mb-8"></div>
  <div class="flex items-center justify-center space-x-6">
    <p class="text-xl font-medium tracking-wide">数据科学概论课程大作业</p>
    <p class="text-lg opacity-80">2024-2025学年第一学期</p>
  </div>
</div>

<style>
.slidev-layout {
  background-image: url('https://images.unsplash.com/photo-1519003722824-194d4455a60c?auto=format&fit=crop&w=1920&q=80');
  background-size: cover;
  background-position: center;
  position: relative;
}

.slidev-layout::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5));
}

@keyframes fade-in {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fade-in 1s ease-out forwards;
}

.custom-title {
  font-size: 3.5rem !important;
}

</style>
