<template>
  <!-- Main Section -->
  <section class="w-full px-5 lg:px-20 py-12 lg:py-20">

    <!-- Main Flex -->
    <div class="flex flex-col-reverse lg:flex-row items-center gap-10 lg:gap-16">

      <!-- Left Content -->
      <div class="w-full lg:w-[50%]">

        <h1 class="text-3xl sm:text-5xl md:text-6xl lg:text-3xl text-yellow-600 leading-tight">
          Let Us Take You to Your Dream Home
        </h1>

        <div class="mt-5 text-[14px] sm:text-[15px] leading-7 sm:leading-8 text-gray-700">
          <p class="mb-4">
            At Per Square Feet, we believe that finding the right home is one
            of the most important decisions in a person's life.
          </p>

          <p class="mb-4">
            Per Square Feet is a leading real estate agency in Bangalore,
            supported by experienced professionals.
          </p>

          <p>
            With over five years of experience in the diversified real estate
            sector, Per Square Feet has built a strong reputation.
          </p>
        </div>

        <!-- Button -->
        <router-link to="/projects">
          <button class="mt-6 bg-black text-white px-6 py-3 rounded-2xl text-sm sm:text-base">
            <router-link to="/about-us">Discover →</router-link>
          </button>
        </router-link>

      </div>

      <!-- Right Image -->
      <div class="w-full lg:w-[45%]">

        <img src="/files/kitchenimage.png" alt="Interior"
          class="w-full h-[300px] sm:h-[400px] md:h-[500px] lg:h-[450px] object-cover rounded-3xl shadow-lg" />

      </div>

    </div>

  </section>
</template>