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

        <Transition name="lightbox">
       
     <div
    v-if="selectedImage"
    class="fixed inset-0 bg-black/90 z-50 flex items-center justify-center">

    

    <!-- Previous -->
    <button
    @click="prevImage"
    class="absolute left-6 z-20 w-12 h-12 rounded-full bg-white/20 hover:bg-white/35 transition-all duration-300 flex items-center justify-center backdrop-blur-sm"
>
    <span class="material-symbols-outlined text-white text-[28px]">
        chevron_left
    </span>
</button>

   <div class="relative inline-block">

    <!-- Image -->
    <img
        :src="selectedImage.src"
        class="max-w-[90vw] max-h-[85vh] rounded-xl object-contain" />

    <!-- Close Button -->
    <button
        @click="closeViewer"
        class="absolute top-[-9px] right-[-2px] z-50 w-12 h-12 rounded-full bg-black/60 hover:bg-black/80 text-white flex items-center justify-center">

        <span class="text-4xl leading-none">&times;</span>

    </button>

</div>

    <!-- Next -->
    <button
        @click="nextImage"
        class="absolute right-5 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 text-white rounded-full w-12 h-12 flex items-center justify-center">

        <span class="material-symbols-outlined">
            arrow_forward_ios
        </span>

    </button>

</div>
        </Transition>

    </div>
</template>

<script setup>
import { ref, computed, onMounted,onUnmounted } from "vue";
import axios from "axios";


const categories = [
    "All",
    "Exterior",
    "Interior",
    "Amenities",
    "Master Plan",
];

const selectedCategory = ref("All");
const images = ref([]);
const selectedImage = ref(null);

const getGalleryImages = async () => {
    try {
        const response = await axios.get(
            "/api/method/per_sqr_ft.api.gallery.get_gallery_images"
        );

        images.value = response.data.message.map(item => ({
            src: item.image,
            category: item.category,
            title: item.title
        }));

    } catch (error) {
        console.error("Error fetching gallery images:", error);
    }
};

onMounted(() => {
    getGalleryImages();
    window.addEventListener("keydown", handleKeydown);
});

const filteredImages = computed(() => {
    if (selectedCategory.value === "All") {
        return images.value;
    }

    return images.value.filter(
        (img) => img.category === selectedCategory.value
    );
});

// const openImage = (image) => {
//     selectedImage.value = image;
// };

const currentIndex = ref(0);

const openImage = (image) => {
    currentIndex.value = filteredImages.value.findIndex(
        (img) => img.src === image.src
    );

    selectedImage.value = filteredImages.value[currentIndex.value];
};

const nextImage = () => {
    currentIndex.value =
        (currentIndex.value + 1) % filteredImages.value.length;

    selectedImage.value = filteredImages.value[currentIndex.value];
};

const prevImage = () => {
    currentIndex.value =
        (currentIndex.value - 1 + filteredImages.value.length) %
        filteredImages.value.length;

    selectedImage.value = filteredImages.value[currentIndex.value];
};

const closeViewer = () => {
    selectedImage.value = null;
};


const handleKeydown = (e) => {
    if (!selectedImage.value) return;

    switch (e.key) {
        case "ArrowRight":
            nextImage();
            break;

        case "ArrowLeft":
            prevImage();
            break;

        case "Escape":
            closeViewer();
            break;
    }
};


onUnmounted(() => {
    window.removeEventListener("keydown", handleKeydown);
});
</script>
<style scoped>
.lightbox-enter-active,
.lightbox-leave-active {
    transition: all .35s ease;
}

.lightbox-enter-from,
.lightbox-leave-to {
    opacity: 0;
    transform: scale(.9);
}

.lightbox-enter-to,
.lightbox-leave-from {
    opacity: 1;
    transform: scale(1);
}
</style>
