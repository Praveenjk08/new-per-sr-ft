<template>
  <!-- Amenities Section -->
  <section class="py-2 px-5 lg:px-20 bg-[#f8fafc]">

    <!-- Heading -->
    <div class="text-center mb-14">

      <h1 class="text-3xl sm:text-5xl lg:text-4xl font-bold text-[#0B1560]">
        Premium Amenities
      </h1>

      <p class="text-gray-500 mt-4 text-base sm:text-lg">
        Experience luxury lifestyle with world-class facilities
      </p>

    </div>

    <!-- Amenities Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-6">

      <!-- Card -->
      <div v-for="item in amenities" :key="item.name"
        class="group bg-white rounded-3xl p-8 flex flex-col items-center justify-center shadow-lg hover:shadow-2xl hover:-translate-y-3 transition-all duration-500 border border-gray-100">

        <!-- Icon Box -->
        <div
          class="w-[150px] h-[150px] rounded-3xl bg-gradient-to-br bg-white flex items-center justify-center  transition duration-500">

          <!-- Icon -->
          <img :src="item.icon" :alt="item.name" class="w-full h-full object-cover" />

        </div>

        <!-- Title -->
        <h2 class="mt-6 text-sm sm:text-lg font-semibold text-gray-800 text-center">
          {{ item.name }}
        </h2>

      </div>

    </div>

  </section>
</template>

<script setup>
const amenities = [
  {
    name: "24/7 Security",
    icon: new URL(
      "/files/securityanimation.png",
      import.meta.url
    ).href,
  },

  {
    name: "Swimming Pool",
    icon: new URL(
      "/files/pool.png",
      import.meta.url
    ).href,
  },

  {
    name: "Kids Play Area",
    icon: new URL(
      "/files/playground.png",
      import.meta.url
    ).href,
  },

  {
    name: "Gymnasium",
    icon: new URL(
      "/files/gym.png",
      import.meta.url
    ).href,
  },

  {
    name: "Car Parking",
    icon: new URL(
      "/files/parking.png",
      import.meta.url
    ).href,
  },

  {
    name: "Jogging Track",
    icon: new URL(
      "/files/jogging.png",
      import.meta.url
    ).href,
  },

  {
    name: "Indoor Games",
    icon: new URL(
      "/files/indoor-games.png",
      import.meta.url
    ).href,
  },

  {
    name: "Power Backup",
    icon: new URL(
      "/files/power.png",
      import.meta.url
    ).href,
  },

  {
    name: "Garden",
    icon: new URL(
      "/files/garden.png",
      import.meta.url
    ).href,
  },

  {
    name: "Rain Water Harvest",
    icon: new URL(
      "/files/rainwater.png",
      import.meta.url
    ).href,
  },
];
</script>