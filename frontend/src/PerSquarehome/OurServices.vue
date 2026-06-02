<template>
  <section class="py-16 px-4 sm:px-6 lg:px-10 bg-[#f8f8f8]">

    <!-- Heading -->
    <div class="text-center mb-14">
      <p class="text-[#4b4b9b] font-semibold text-lg">
        Top Real Estate Services
      </p>

      <h2
        class="text-3xl sm:text-4xl font-bold text-[#2f2f68] mt-3 leading-tight"
      >
        Presenting Best Real Estate Services
      </h2>
    </div>

    <!-- Cards -->
    <div
      class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8"
    >

      <!-- Card 1 -->
      <div
        class="bg-white rounded-3xl shadow-lg p-10 text-center hover:-translate-y-2 transition duration-300"
      >
        <div class="text-7xl text-[#4b4b9b] mb-8">
          🏠
        </div>

        <h3 class="text-2xl font-semibold text-[#2f2f68] mb-5">
          Real Estate Consultation
        </h3>

        <p class="text-gray-600 leading-9 text-lg">
          Get personalized real estate advice from our experts for
          buying, selling, renting, and investment opportunities.
        </p>

        <router-link
          to="/real estate consultation"
          class="inline-flex items-center gap-2 mt-8 text-lg font-medium text-black hover:text-[#4b4b9b]"
        >
          Read More →
        </router-link>
      </div>

      <!-- Card 2 -->
      <div
        class="bg-white rounded-3xl shadow-lg p-10 text-center hover:-translate-y-2 transition duration-300"
      >
        <div class="text-7xl text-[#4b4b9b] mb-8">
          💰
        </div>

        <h3 class="text-2xl font-semibold text-[#2f2f68] mb-5">
          Housing Loan Services
        </h3>

        <p class="text-gray-600 leading-9 text-lg">
          Secure the best home loan solutions with easy documentation,
          flexible EMI options, and expert financial guidance.
        </p>

        <router-link
          to="/housing-loan"
          class="inline-flex items-center gap-2 mt-8 text-lg font-medium text-black hover:text-[#4b4b9b]"
        >
          Read More →
        </router-link>
      </div>

      <!-- Card 3 -->
      <div
        class="bg-white rounded-3xl shadow-lg p-10 text-center hover:-translate-y-2 transition duration-300"
      >
        <div class="text-7xl text-[#4b4b9b] mb-8">
          🛋️
        </div>

        <h3 class="text-2xl font-semibold text-[#2f2f68] mb-5">
          Interior Design Services
        </h3>

        <p class="text-gray-600 leading-9 text-lg">
          Transform your home with elegant, modern, and functional
          interior design solutions tailored to your lifestyle.
        </p>

        <router-link
          to="/interior"
          class="inline-flex items-center gap-2 mt-8 text-lg font-medium text-black hover:text-[#4b4b9b]"
        >
          Read More →
        </router-link>
      </div>

      <!-- Card 4 -->
      <div
        class="bg-white rounded-3xl shadow-lg p-10 text-center hover:-translate-y-2 transition duration-300"
      >
        <div class="text-7xl text-[#4b4b9b] mb-8">
          ⚖️
        </div>

        <h3 class="text-2xl font-semibold text-[#2f2f68] mb-5">
          Legal Consultation
        </h3>

        <p class="text-gray-600 leading-9 text-lg">
          Handle legal documentation, verification, and registration
          processes smoothly with professional legal support.
        </p>

        <router-link
          to="/legal"
          class="inline-flex items-center gap-2 mt-8 text-lg font-medium text-black hover:text-[#4b4b9b]"
        >
          Read More →
        </router-link>
      </div>

      <!-- Card 5 -->
      <div
        class="bg-white rounded-3xl shadow-lg p-10 text-center hover:-translate-y-2 transition duration-300"
      >
        <div class="text-7xl text-[#4b4b9b] mb-8">
          🏢
        </div>

        <h3 class="text-2xl font-semibold text-[#2f2f68] mb-5">
          Property Management
        </h3>

        <p class="text-gray-600 leading-9 text-lg">
          Complete property management solutions including maintenance,
          rentals, tenant support, and property supervision.
        </p>

        <router-link
          to="/property-management"
          class="inline-flex items-center gap-2 mt-8 text-lg font-medium text-black hover:text-[#4b4b9b]"
        >
          Read More →
        </router-link>
      </div>

      <!-- Card 6 -->
      <div
        class="bg-white rounded-3xl shadow-lg p-10 text-center hover:-translate-y-2 transition duration-300"
      >
        <div class="text-7xl text-[#4b4b9b] mb-8">
          🏗️
        </div>

        <h3 class="text-2xl font-semibold text-[#2f2f68] mb-5">
          Construction Services
        </h3>

        <p class="text-gray-600 leading-9 text-lg">
          High-quality residential and commercial construction services
          designed with durability, innovation, and excellence.
        </p>

        <router-link
          to="/construction"
          class="inline-flex items-center gap-2 mt-8 text-lg font-medium text-black hover:text-[#4b4b9b]"
        >
          Read More →
        </router-link>
      </div>

    </div>

  </section>
</template>