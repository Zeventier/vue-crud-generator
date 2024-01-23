<template>
  <AppLayout title="__Title__">
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 leading-tight">
        __Title__ Details
      </h2>
    </template>
    <div class="container">
      <div class="row">
        <div class="col-md-6 offset-md-3">
          <a
            class="btn btn-primary mb-3 mt-3"
            :href="route('admin.__table__.index')"
            ><font-awesome-icon icon="fa-solid fa-arrow-left"
          /></a>
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Detail __Title__</h5>

              <p class="card-text">__Field__: {{ __table__.__field__ }}</p>

              <a :href="route('admin.__table__.edit', __table__)"><jet-primary-button class="m-1">
                  <font-awesome-icon icon="fa-solid fa-pen-to-square" />
                </jet-primary-button></a>
              <jet-danger-button class="m-1" @click="delete_item(__table__)">
                <font-awesome-icon icon="fa-solid fa-trash-can" />
              </jet-danger-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script>
import { useForm } from "@inertiajs/vue3";
import AppLayout from "@/Layouts/AppLayout.vue";
import JetDangerButton from "@/Components/DangerButton.vue";
import JetPrimaryButton from "@/Components/PrimaryButton.vue";

export default {
  components: {
    AppLayout,
    JetDangerButton,
    JetPrimaryButton,
  },
  props: {
    __table__: {
      type: Object,
    },
  },
  setup() {
    const form = useForm({});

    const delete_item = (__table__) => {
      if (confirm("Are you sure you want to delete this __table__?")) {
        form.delete(route("admin.__table__.delete", __table__.id));
      }
    };

    return {
      form,
      delete_item,
    };
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
