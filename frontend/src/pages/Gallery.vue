<!-- <template>


    <section class="w-full h-[500px]">

        <div class="group relative max-w-7xl mx-auto px-4 text-center">
            <h1 class="text-3xl font-bold text-[#156082] mb-6">Gallery</h1>
            <p class="text-lg text-gray-700 mb-4">Welcome to our gallery! Here you can view our latest projects and
                achievements.</p>
        </div>

    </section>


</template> -->

<template>
    <div class="bg-gray-50 min-h-screen">

        <!-- Hero Section -->
        <section class="py-4 text-center">
            <h1 class="text-[18px] font-bold text-gray-900">
                Gallery
            </h1>
            <div class="h-1 w-24 bg-orange-500 rounded-full mx-auto mt-3"></div>

            <p class="mt-3 text-gray-600 ">
                Discover the beauty and elegance of our featured projects.
            </p>
        </section>

        <!-- Filters -->
        <div class="container mx-auto px-6 py-4">
            <div class="flex flex-wrap gap-3 justify-center">

                <button v-for="category in categories" :key="category" @click="selectedCategory = category"
                    class="px-4 py-1 rounded-full border text-[14px] transition" :class="selectedCategory === category
                        ? 'bg-orange-500 text-white border-orange-500'
                        : 'bg-white text-gray-700 border-gray-200 hover:bg-orange-50'
                        ">
                    {{ category }}
                </button>

            </div>
        </div>

        <!-- Gallery Grid -->
        <div class="container mx-auto px-6 pb-12">

            <div class="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <div v-for="(image, index) in filteredImages" :key="index"
                    class="group overflow-hidden rounded-2xl shadow-md bg-white cursor-pointer"
                    @click="openImage(image)">
                    <img :src="image.src" :alt="image.category"
                        class="w-full h-[160px] md:h-[250px] object-cover transition duration-500 group-hover:scale-110" />
                    <div class="p-4">
                        <p class="text-gray-700 font-medium">
                            {{ image.category }}
                        </p>
                    </div>
                </div>

            </div>

        </div>

        <!-- Lightbox -->
        <div v-if="selectedImage" class="fixed inset-0 bg-black/90 z-50 flex items-center justify-center p-6"
            @click="selectedImage = null">
            <img :src="selectedImage.src" class="max-w-full max-h-[90vh] rounded-xl" />
        </div>

    </div>
</template>

<script setup>
import { ref, computed } from "vue";

const categories = [
    "All",
    "Exterior",
    "Interior",
    "Amenities",
    "Master Plan",
];

const selectedCategory = ref("All");

const images = ref([
    {
        src: "/files/Interior-1.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-2.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-3.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-4.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-5.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-6.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-7.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-23.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-9.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-10.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-11.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-12.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-13.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-14.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-15.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-16.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-17.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-18.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-19.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-20.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-21.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-22.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-23.jpg",
        category: "Interior",
    },
    {
        src: "/files/Interior-25.jpg",
        category: "Interior",
    },
    {
        src: "/files/Exterior-1.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-2.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-3.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-4.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-5.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-6.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-7.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-8.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-9.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-10.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-11.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-12.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-13.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-14.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Exterior-15.jpg",
        category: "Exterior",
    },
    {
        src: "/files/Amenities-1.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-2.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-3.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-4.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-5.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-6.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-7.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-8.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-9.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-10.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-11.jpg",
        category: "Amenities",
    },
    {
        src: "/files/Amenities-12.jpg",
        category: "Amenities",
    },

]);

const filteredImages = computed(() => {
    if (selectedCategory.value === "All") {
        return images.value;
    }

    return images.value.filter(
        (img) => img.category === selectedCategory.value
    );
});

const selectedImage = ref(null);

const openImage = (image) => {
    selectedImage.value = image;
};
</script>
