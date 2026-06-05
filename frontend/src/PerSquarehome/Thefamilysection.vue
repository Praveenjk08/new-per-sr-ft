<template>
  <!-- Main Section -->
  <section class="w-full py-10 px-4 sm:px-6 lg:px-16 bg-white">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

      <!-- Left Image -->
      <div class="flex justify-center">
        <img src="/files/family-photo-home.jpg" alt="Family"
          class="w-full h-[500px] max-w-[550px] rounded-3xl shadow-lg object-cover" />
      </div>

      <!-- Right Content -->
      <div>
        <h1 class="text-3xl sm:text-5xl lg:text-3xl text-yellow-950 mb-6">
          Helping You Secure Your Dream Home
        </h1>

        <div class="text-[14px] text-black leading-8 space-y-1">

          <p>
            A home is more than just a place to live it is a space where comfort,
            security, and happiness come together. It is where memories are created,
            families grow, and life finds its true meaning. In today's fast-paced world,
            life may take you to many unexpected places, but in the end, love always
            brings you back home with Per Square Feet.
          </p>

          <p>
            At Per Square Feet, we understand the emotional and financial importance
            of owning the perfect home. Our mission is to help individuals and families
            find properties that not only meet their needs but also fulfill their dreams
            of a better lifestyle. We carefully select and present some of the most
            premium and well-planned real estate projects across Bangalore, ensuring
            that our clients receive the best options available in the market.
          </p>

          <p>
            What truly sets Per Square Feet apart is our commitment to delivering
            world-class sales and marketing services while maintaining transparency,
            trust, and customer satisfaction.
          </p>

        </div>

        <!-- Button -->
        <router-link to="/about-us" custom v-slot="{ navigate }">
          <button @click="navigate"
            class="mt-8 flex items-center gap-2 bg-[#1A1A1A] hover:bg-black transition-all duration-300 text-white px-6 py-3 rounded-xl text-sm font-medium shadow-md">
            About Us

            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="w-4 h-4">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
            </svg>
          </button>
        </router-link>
      </div>
    </div>
  </section>
</template>