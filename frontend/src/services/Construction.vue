<template>
<!-- Hero Section -->
<section class="px-4 sm:px-6 lg:pl-10 my-8">

  <div
    class="relative w-full h-[400px] sm:h-[500px] lg:h-[650px] overflow-hidden rounded-[40px]"
  >

    <!-- Background Image -->
    <img
      src="/files/constructionbannerimage.png"
      alt="Construction"
      class="w-full h-full object-cover"
    />

    <!-- Dark Overlay -->
    <div class="absolute inset-0rounded-[40px]"></div>

    <!-- Content -->
    <div
      class="absolute inset-0 flex flex-col items-center justify-center text-center px-6"
    >

      <h1
        class="text-shadow-yellow-400 text-2xl sm:text-5xl lg:text-2xl font-bold leading-tight"
      >
        Building Dreams <br />
        With Quality Construction
      </h1>

      <p
        class="text-white/90 text-sm sm:text-lg lg:text-xl mt-5 max-w-3xl leading-4 md:leading-8"
      >
        We deliver modern, durable, and innovative construction solutions
        designed to create strong foundations and beautiful living spaces
        for the future.
      </p>

      <button @click="goToProjects"
        class="mt-8 bg-orange-500 hover:bg-orange-600 text-white px-8 py-3 rounded-full text-lg transition duration-300"
      >
        Explore Projects
      </button>

    </div>

  </div>

</section>

  <!-- About Construction -->
  <section class="w-full py-16 px-5 lg:px-20 bg-white">

    <div
      class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center"
    >

      <!-- Left Content -->
      <div>

        <p
          class="text-[#d49a37c9] text-[18px] font-semibold uppercase tracking-[2px]"
        >
          About Construction
        </p>

        <h1
          class="text-[30px] sm:text-[30px] font-bold text-[#0B1560] mt-3"
        >
          Trusted Construction Solutions
        </h1>

        <p
          class="text-[15px] text-gray-600 leading-8 mt-6"
        >
          At Per Square Feet, we deliver premium construction
          services designed to create modern, durable, and
          elegant living spaces. Our experienced team focuses
          on quality, innovation, and timely project delivery.
        </p>

        <p
          class="text-[15px] text-gray-600 leading-8 mt-5"
        >
          From residential homes to commercial projects, we
          ensure every structure is built with precision,
          advanced technology, and customer satisfaction at
          the core of our work.
        </p>

      </div>

      <!-- Right Image -->
      <div>

        <img
          src="/files/Constructionrightsideiamge.png"
          alt="Construction Work"
          class="w-full h-[350px] sm:h-[500px] object-cover rounded-[35px] shadow-xl"
        />

      </div>

    </div>

  </section>

  <!-- Services -->
  <section
    class="relative left-1/2 right-1/2 -mx-[50vw] w-screen bg-[#f8fafc] py-16"
  >

    <div class="px-5 lg:px-20">

      <div class="text-center mb-12">

        <p
          class="text-[#d49a37c9] text-[18px] font-semibold uppercase tracking-[2px]"
        >
          Our Services
        </p>

        <h1
          class="text-[30px] sm:text-[30px] font-bold text-[#0B1560] mt-3"
        >
          What We Provide
        </h1>

      </div>

      <!-- Service Cards -->
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8"
      >

        <!-- Card -->
        <div
          class="bg-white rounded-[30px] p-10 shadow-lg"
        >

          <h2
            class="text-[22px] font-bold text-[#156082]"
          >
            Residential Construction
          </h2>

          <p
            class="text-[15px] text-gray-600 leading-7 mt-5"
          >
            Premium homes, villas, and apartments built with
            modern designs and high-quality materials.
          </p>

        </div>

        <!-- Card -->
        <div
          class="bg-white rounded-[30px] p-10 shadow-lg"
        >

          <h2
            class="text-[22px] font-bold text-[#156082]"
          >
            Commercial Construction
          </h2>

          <p
            class="text-[15px] text-gray-600 leading-7 mt-5"
          >
            Smart commercial spaces designed for businesses,
            offices, and retail developments.
          </p>

        </div>

        <!-- Card -->
        <div
          class="bg-white rounded-[30px] p-10 shadow-lg"
        >

          <h2
            class="text-[22px] font-bold text-[#156082]"
          >
            Renovation & Remodeling
          </h2>

          <p
            class="text-[15px] text-gray-600 leading-7 mt-5"
          >
            Modern renovation solutions that transform old
            spaces into stylish and functional environments.
          </p>

        </div>

      </div>

    </div>

  </section>

  <!-- Why Choose Us -->
  <section class="w-full py-16 px-5 lg:px-20 bg-white">

    <div class="text-center mb-12">

      <p
        class="text-[#d49a37c9] text-[18px] font-semibold uppercase tracking-[2px]"
      >
        Why Choose Us
      </p>

      <h1
        class="text-[30px] sm:text-[30px] font-bold text-[#0B1560] mt-3"
      >
        Excellence In Every Project
      </h1>

    </div>

    <div
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8"
    >

      <!-- Card -->
      <div
        class="bg-[#f8fafc] rounded-[25px] p-8 shadow-lg text-center"
      >

        <h2
          class="text-[18px] font-bold text-[#156082]"
        >
          Quality Materials
        </h2>

        <p
          class="text-[15px] text-gray-600 leading-7 mt-4"
        >
          We use premium materials for strong and durable
          construction.
        </p>

      </div>

      <!-- Card -->
      <div
        class="bg-[#f8fafc] rounded-[25px] p-8 shadow-lg text-center"
      >

        <h2
          class="text-[18px] font-bold text-[#156082]"
        >
          Expert Team
        </h2>

        <p
          class="text-[15px] text-gray-600 leading-7 mt-4"
        >
          Experienced engineers and professionals managing
          every project.
        </p>

      </div>

      <!-- Card -->
      <div
        class="bg-[#f8fafc] rounded-[25px] p-8 shadow-lg text-center"
      >

        <h2
          class="text-[18px] font-bold text-[#156082]"
        >
          Timely Delivery
        </h2>

        <p
          class="text-[15px] text-gray-600 leading-7 mt-4"
        >
          Projects completed on schedule with complete
          customer satisfaction.
        </p>

      </div>

      <!-- Card -->
      <div
        class="bg-[#f8fafc] rounded-[25px] p-8 shadow-lg text-center"
      >

        <h2
          class="text-[18px] font-bold text-[#156082]"
        >
          Modern Design
        </h2>

        <p
          class="text-[15px] text-gray-600 leading-7 mt-4"
        >
          Elegant architectural solutions with innovative
          construction methods.
        </p>

      </div>

    </div>

  </section>

  <!-- CTA -->
  <section
    class="relative left-1/2 right-1/2 -mx-[50vw] w-screen bg-[#0B1560] py-16"
  >

    <div class="text-center px-5">

      <h1
        class="text-white text-[32px] sm:text-[45px] font-bold"
      >
        Ready To Build Your Dream Project?
      </h1>

      <p
        class="text-white/80 text-[15px] leading-8 mt-5 max-w-2xl mx-auto"
      >
        Contact Per Square Feet today for premium
        construction services and trusted project execution.
      </p>

      <button
        @click="goToContact"
        class="mt-8 bg-[#d49a37c9] hover:bg-[#d49a37] text-white px-8 py-4 rounded-2xl text-[16px] font-semibold transition duration-300"
      >
        Contact Us
      </button>

    </div>

  </section>

</template>
<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goToContact = () => {
  router.push("/contact-us");
};


const goToProjects = () => {
  router.push("/projects");
};

</script>