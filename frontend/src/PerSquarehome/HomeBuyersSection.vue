<template>
    <section class="max-w-7xl mx-auto py-8 px-4">

        <div class="text-center mb-10">
            <h2 class="text-4xl font-semibold">
                Happy <span class="text-[#d4b46a]">Home</span>owners </h2>

            <p class="text-xl text-gray-600 mt-2">
                Real Stories from Families Who Found Their Dream Homes
            </p>
        </div>

        <div class="bg-[#f5f5f5] rounded-3xl p-6">

            <div class="grid lg:grid-cols-[35%_65%] gap-6">

                <!-- LEFT SIDE -->
                <div class="bg-white rounded-2xl overflow-hidden shadow">

                    <img :src="buyers[currentIndex].image" :alt="buyers[currentIndex].name"
                        class="w-full h-[320px] object-cover" />

                    <div class="text-center py-5 px-4">

                        <h3 class="text-3xl font-semibold">
                            {{ buyers[currentIndex].name }}
                        </h3>

                        <p class="text-gray-600 mt-2">
                            {{ buyers[currentIndex].property }}
                        </p>

                        <p class="text-gray-500">
                            {{ buyers[currentIndex].location }}
                        </p>

                    </div>

                    <!-- Controls -->
                    <div class="flex justify-center gap-4 pb-5">
                        <button @click="prevSlide" class="w-10 h-10 rounded-full bg-gray-200 hover:bg-gray-300">
                            ‹
                        </button>

                        <button @click="nextSlide" class="w-10 h-10 rounded-full bg-gray-200 hover:bg-gray-300">
                            ›
                        </button>
                    </div>

                </div>

                <!-- RIGHT SIDE -->
                <div class="bg-white rounded-2xl p-6 shadow">

                    <div class="grid md:grid-cols-2 gap-4">

                        <div v-for="review in reviews" :key="review.name"
                            class="bg-white rounded-3xl border border-[#d4b46a] p-5 relative">

                            <div class="flex justify-between">

                                <div class="flex gap-3">

                                    <div
                                        class="w-12 h-12 rounded-full bg-teal-600 text-white flex items-center justify-center">
                                        {{ review.name.charAt(0) }}
                                    </div>

                                    <div>
                                        <h4 class="font-semibold">
                                            {{ review.name }}
                                        </h4>

                                        <p class="text-sm text-gray-500">
                                            {{ review.time }}
                                        </p>
                                    </div>

                                </div>

                                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg"
                                    class="w-5 h-5" />
                            </div>

                            <div class="mt-3 text-yellow-500">
                                ⭐⭐⭐⭐⭐
                            </div>

                            <p class="mt-3 text-gray-700 leading-7">
                                {{
                                    review.expanded
                                        ? review.comment
                                        : review.comment.slice(0, 100)
                                }}
                                <span v-if="
                                    !review.expanded &&
                                    review.comment.length > 100
                                ">
                                    ...
                                </span>
                            </p>

                            <button v-if="review.comment.length > 100" @click="review.expanded = !review.expanded"
                                class="mt-3 text-gray-500">
                                {{
                                    review.expanded
                                        ? "Read Less"
                                        : "Read More"
                                }}
                            </button>

                            <div class="absolute bottom-2 right-4 text-[#d4b46a] text-5xl">
                                “
                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const currentIndex = ref(0);

const buyers = ref([
    {
        image: "/files/certifiacteslid1.jpeg",
        name: "Dr. Shiva & Family",
        property: "3 BHK Flat",
        location: "Bangalore"
    },
    {
        image: "/files/certifiacteslid2.jpeg",
        name: "Ravi Kumar",
        property: "Villa",
        location: "Whitefield"
    },
    {
        image: "/files/certifiacteslid3.jpeg",
        name: "Priya Sharma",
        property: "Apartment",
        location: "Sarjapur"
    }
]);

const reviews = ref([
    {
        name: "Suresh",
        time: "2 months ago",
        comment:
            "Excellent service and best pricing. The team guided us throughout the entire process.",
        expanded: false
    },
    {
        name: "Ravi",
        time: "1 month ago",
        comment:
            "Very professional and helpful team. We got the best deal through them.",
        expanded: false
    },
    {
        name: "Priya",
        time: "3 months ago",
        comment:
            "Smooth buying experience and complete support till registration.",
        expanded: false
    },
    {
        name: "Shivu",
        time: "2 months ago",
        comment:
            "Excellent service and quick response whenever we needed assistance.",
        expanded: false
    }
]);

const nextSlide = () => {
    currentIndex.value =
        (currentIndex.value + 1) % buyers.value.length;
};

const prevSlide = () => {
    currentIndex.value =
        (currentIndex.value - 1 + buyers.value.length) %
        buyers.value.length;
};

let interval;

onMounted(() => {
    interval = setInterval(nextSlide, 5000);
});

onBeforeUnmount(() => {
    clearInterval(interval);
});
</script>