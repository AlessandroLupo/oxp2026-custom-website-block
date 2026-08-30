import { BuilderAction } from "@html_builder/core/builder_action";
import { Plugin } from "@html_editor/plugin";
import { registry } from "@web/core/registry";

class WeatherOptionPlugin extends Plugin {
    static id = "weatherOption";
    resources = {
        builder_actions: {
            WeatherAddBannerAction,
        },
        has_overlay_options: { hasOption: (el) => el.matches(".weather-banner") },
    };
}

export class WeatherAddBannerAction extends BuilderAction {
    static id = "weatherAddBanner";

    apply({ editingElement }) {
        const bannerEl = document.createElement("div");
        bannerEl.className = "weather-banner row justify-content-center bg-warning-subtle border border-warning-subtle rounded-3 mt-2 py-2";
        bannerEl.textContent = "🕶️ Remember your sun glasses!";
        editingElement.querySelector(".container").appendChild(bannerEl);
    }
}

registry.category("website-plugins").add(WeatherOptionPlugin.id, WeatherOptionPlugin);
