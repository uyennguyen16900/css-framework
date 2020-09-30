class TabsGroup extends HTMLElement {
  constructor() {
    super();

    this.state = {
      activeTabIndex: -1,
      maxIndex: 0
    };

    // Stores for triggers and panels
    this.triggers = [];
    this.panels = [];
  }

  connectedCallback() {
    this.initialTriggers = [...this.querySelectorAll('[data-element="trigger"]')];
    this.initialPanels = [...this.querySelectorAll('[data-element="panel"]')];

    // Run the renderer to render the new tabs HTML in the shadow root
    this.render();
  }

  // Generates the component HTML and then renders it to the shadow root
  render = async () => {
    const trigger = (text, index) => {
      return `
        <button class="tabs__button" data-index="${index}" data-element="trigger-button" role="tab">${text}</button>
      `;
    };

    const panel = (html, index) => {
      return `
        <article class="tabs__panel" data-index="${index}" data-element="panel">${html}</article>
      `;
    };

    try {
      const stylesRequest = await fetch('./css/tabs-group.css');

      if (![200, 304].includes(stylesRequest.status)) {
        return Promise.reject('Error loading CSS');
      }

      const styles = await stylesRequest.text();

      const template = `
      <style>${styles}</style>
      <div class="tabs">
        <ul role="tablist" class="tabs__triggers">
          ${this.initialTriggers
            .map((item, index) => `<li>${trigger(item.innerText, index)}</li>`)
            .join('')}          
        </ul>
        ${this.initialPanels.map((item, index) => panel(item.innerHTML, index)).join('')}
      </div>
    `;

      // Set our root as a new open shadow root. This makes
      // rendering and setting HTML easier because we have a
      // class-level element to work with
      this.root = this.attachShadow({mode: 'open'});

      // Clear light DOM
      this.innerHTML = '';

      this.root.innerHTML = template;

      this.postRender();
    } catch (ex) {
      console.error(ex);
    }
  };

  postRender() {
    this.triggers = this.root.querySelectorAll('[data-element="trigger-button"]');
    this.panels = this.root.querySelectorAll('[data-element="panel"]');

    // Remove the triggers and bail out if there's a mismatch of triggers and panels.
    // It’s better to leave the element mostly like it was, rather than have a broken component
    if (this.triggers.length !== this.panels.length) {
      this.triggers.forEach(trigger => trigger.parentNode.removeChild(trigger));
      return;
    }

    // We know we're all good so set the first item as active and set max index
    this.state.maxIndex = this.triggers.length - 1;
    this.toggle(0, true);

    // Now set each trigger’s events
    this.triggers.forEach((trigger, triggerIndex) => {
      // On click, show this trigger’s panel
      trigger.addEventListener('click', evt => {
        evt.preventDefault();

        this.toggle(triggerIndex);
      });

      trigger.addEventListener('keydown', evt => {
        switch (evt.keyCode) {
          case 39:
            this.modifyIndex('up', triggerIndex);
            break;
          case 37:
            this.modifyIndex('down', triggerIndex);
            break;
          case 40:
            // If the down key is pressed, we want to focus on the active panel
            this.panels[triggerIndex].focus();
            break;
        }
      });
    });

    // Lastly, set the panel’s events
    this.panels.forEach(panel => {
      panel.addEventListener('keydown', evt => {
        switch (evt.keyCode) {
          case 38:
            // When the user keys up (when this is focused), focus on it's related tab
            this.triggers[this.state.activeTabIndex].focus();
            break;
        }
      });
    });
  }

  toggle(index, isInitial = false) {
    // If the passed index is the same as the active index
    // we don't need to do anything, so bail
    if (index === this.state.activeTabIndex) {
      return;
    }

    // If the index has been exceeded, let's just set it to
    // the maxIndex
    if (index > this.state.maxIndex) {
      index = this.state.maxIndex;
    }

    this.state.activeTabIndex = index;

    this.triggers.forEach((trigger, triggerIndex) => {
      const panel = this.panels[triggerIndex];

      if (triggerIndex === index) {
        trigger.setAttribute('aria-selected', 'true');

        // Remove the tabindex override so it can be focussed with
        // the keyboard again
        trigger.removeAttribute('tabindex');

        // Focus this trigger if this isn’t the initial toggle
        // because other triggers are now focus-proof
        if (!isInitial) {
          trigger.focus();
        }

        // Show the panel and add a tabindex so it can be
        // programatically focused
        panel.setAttribute('data-state', 'visible');
        panel.setAttribute('tabindex', '-1');
      } else {
        // Remove selected state and allow it to be keyboard focused again
        trigger.removeAttribute('aria-selected');
        trigger.setAttribute('tabindex', '-1');

        // Set the panel as hidden and remove tabindex so it can't be
        // programatically focused
        panel.setAttribute('data-state', 'hidden');
        panel.removeAttribute('tabindex');
      }
    });
  }

  modifyIndex(direction, triggerIndex) {
    // We only modify index if we are focused on the active tab or
    // it'll be a confusing user experience
    if (triggerIndex !== this.state.activeTabIndex) {
      return;
    }

    switch (direction) {
      case 'down':
        this.toggle(this.state.activeTabIndex <= 0 ? this.state.maxIndex : this.state.activeTabIndex - 1);
        break;
      case 'up':
        this.toggle(this.state.activeTabIndex >= this.state.maxIndex ? 0 : this.state.activeTabIndex + 1);
        break;
    }
  }
}

if ('customElements' in window) {
  customElements.define('tabs-group', TabsGroup);
}

export default TabsGroup;
