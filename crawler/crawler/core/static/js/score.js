; (function ($, window, document, undefined) {
    "use strict";

    let plugin;
    const PLUGIN_NAME = 'scorepicker';
    const defaultScore = (9)
    const limitScore = 1;

    const template = `
        <div
            class="year-range-picker hidden opacity-0"
        >
            <div class="range-header">
                <div class="range-prev range-control ">
                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M15.3715 4.26035C15.7186 3.91322 16.2814 3.91322 16.6285 4.26035C16.9441 4.57592 16.9728 5.06975 16.7146 5.41773L16.6285 5.51743L10.1464 12L16.6285 18.4826C16.9441 18.7981 16.9728 19.292 16.7146 19.64L16.6285 19.7397C16.313 20.0552 15.8191 20.0839 15.4712 19.8257L15.3715 19.7397L8.26035 12.6285C7.94477 12.313 7.91609 11.8191 8.17428 11.4712L8.26035 11.3715L15.3715 4.26035Z" fill="currentColor"/>
                    </svg>
                </div>
                <div class="selected-range">
                    <span class="text-h5 font-bold text-text-tertiary px-3 py-1.5 year-start"></span>
                    <span class="text-h5 font-bold text-text-primary px-3 py-1.5 year-end"></span>
                </div>
                <div class="range-next range-control">
                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M9.51746 4.26035C9.17032 3.91322 8.60751 3.91322 8.26038 4.26035C7.9448 4.57592 7.91611 5.06975 8.17431 5.41773L8.26038 5.51743L14.7425 12L8.26038 18.4826C7.9448 18.7981 7.91611 19.292 8.17431 19.64L8.26038 19.7397C8.57595 20.0552 9.06978 20.0839 9.41776 19.8257L9.51746 19.7397L16.6286 12.6285C16.9441 12.313 16.9728 11.8191 16.7146 11.4712L16.6286 11.3715L9.51746 4.26035Z" fill="currentColor"/>
                    </svg>
                </div>
            </div>
            <div class="year-ranges"></div>
        </div>
    `;

    function Plugin(element, options) {
        this._element    = element;
        this._pluginName = PLUGIN_NAME;
        this._defaults   = $.fn[PLUGIN_NAME].defaults;
        this._template = template;
        this._maxRangeNumber = limitScore;

        this._minScore = null;
        this._maxScore = null;

        this._startRange = null;
        this._endRange = null;
        this._settings 	 = $.extend({}, this._defaults, options);
        this._init();
    }
    // Avoid Plugin.prototype conflicts
    $.extend(Plugin.prototype, {
        // Initialization logic
        _init: function () {
            plugin = this;

            this._build();
            this._bindEvents();
        },
        // Cache DOM nodes for performance
        _build: function () {
            this.$_element = $(this._element);
            this.$_template = $(this._template);
            this.$_minScore = this._minScore;
            this.$_maxScore = this._maxScore;
            this.$_maxRangeNumber = this._maxRangeNumber;
            this.$_startRange = this._startRange;
            this.$_endRange = this._endRange;

            this._parseElementValue();

            this._generateScoreRange();
            this._generateScoreItems();
            this._generateSelectedClass();

            if (!$('body').find('.score-range-picker').length) {
                $('body').append(this.$_template);
            }
        },
        // Bind events that trigger methods
        _bindEvents: function () {
            plugin.$_element.on('focus' + '.' + plugin._pluginName, function() {
                plugin._setPositionCalendar()
                plugin._showCalendar()
            })

            plugin.$_template.on('click'+ '.' + plugin._pluginName, '.year-item', function(evt) {
                const el = $(this);
                const currentScore = parseFloat(el.text())
                let _startRange = plugin.$_startRange;
                let _endRange = plugin.$_endRange;
                if (_startRange && _endRange) {
                    _startRange = null;
                    _endRange = null;
                }

                if (!_startRange) {
                    _startRange = currentScore
                } else if (!_endRange) {
                    _endRange = currentScore
                }

                if (_startRange && _endRange) {
                    const [start, end] = [_startRange, _endRange].sort();
                    _startRange = start;
                    _endRange = end;
                }

                plugin.$_startRange = _startRange;
                plugin.$_endRange = _endRange;
                plugin._generateSelectedClass();
                plugin._setElementValue();
            })

            plugin.$_template.on('click.' + plugin._pluginName, '.range-control', function(evt) {
                const isNext = $(this).is('.range-next');
                const currentMinScore = plugin.$_minScore;
                const currentMaxScore = plugin.$_maxScore;
                if (isNext) {
                    plugin.$_minScore = currentMaxScore;
                    plugin.$_maxScore = currentMaxScore + plugin._maxRangeNumber;
                } else {
                    plugin.$_minScore = currentMinScore - plugin._maxRangeNumber;
                    plugin.$_maxScore = currentMinScore;
                }
                plugin._generateScoreItems();
                plugin._generateSelectedClass();
            })

            $(document).on('click.' + plugin._pluginName, function (evt) {
                let target = $(evt.target);
                if (
                    target.is(plugin.$_element) ||
                    target.is(plugin.$_template) ||
                    plugin.$_template.has(target).length
                ) {

                    return;
                }
                plugin._hideCalendar();
                plugin._setElementValue();
            })

            $(window).on('resize.' + plugin._pluginName, function (evt) {
                plugin._setPositionCalendar()
            })
        },
        // Unbind events that trigger methods
        _unbindEvents: function () {
            this.$_element.off('.' + this._pluginName);
            this.$_template.off('.' + this._pluginName);
            $(document).off('.' + this._pluginName);
        },
        // Remove plugin instance completely
        _destroy: function () {
            this._unbindEvents();
            this.$_element.removeData();
        },
        // Callback methods
        _callback: function () {
            // Cache onComplete option
            let onComplete = this._settings.onComplete;
            if (typeof onComplete === "function") {
                onComplete(this._element);
            }
        },
        _setPositionCalendar()
        {
            let position = this._getOffset(this.$_element[0])
            let windowWidth = window.outerWidth;

            let calendarComputedStyle = getComputedStyle(plugin.$_template[0]);
            let clientMaxWidth = parseInt(calendarComputedStyle.maxWidth);
            let clientWidth = calendarComputedStyle.width;
            if (clientWidth.indexOf('%') >= 0) {
                clientWidth = windowWidth * (parseInt(clientWidth)/100);
            }
            clientWidth = parseInt(clientWidth);
            let positionLeft = clientWidth >= windowWidth && clientMaxWidth > windowWidth ? 0 : position.left;

            this.$_template.css({
                'position': 'absolute',
                'top': position.bottom + 'px',
                'left': positionLeft + 'px',
            })
        },

        _showCalendar()
        {
            this.$_template.removeClass('hidden opacity-0')
            this.$_template.addClass('block opacity-100')
        },

        _hideCalendar()
        {
            this.$_template.addClass('hidden opacity-0')
            this.$_template.removeClass('block opacity-100')
        },

        _getOffset(el) {
            const rect = el.getBoundingClientRect();
            return {
                left: rect.left + window.scrollX,
                bottom: rect.top + window.scrollY + rect.height
            };
        },

        _generateScoreRange()
        {
            let _defaultScore = defaultScore;
            let anchorStartScore = _defaultScore - 1;
            if (this.$_startRange) {
                let diff = Math.ceil((anchorStartScore - this.$_startRange) / 120)
                _defaultScore = (anchorStartScore - diff * this.$_maxRangeNumber) + 1;
            }
            this.$_minScore = _defaultScore - 1;
            this.$_maxScore = _defaultScore ;
            

        },

        _generateScoreItems()
        {

            if (this.$_minScore < 8){
                this.$_minScore = 8;
                this.$_maxScore = 9;
            }

            if (this.$_maxScore > 10){
                this.$_minScore = 9;
                this.$_maxScore = 10;
            }
            
            let range = this.$_template.find('.year-ranges')
            let items = [];
            for (let i = this.$_minScore; i < this.$_maxScore; i+=0.1) {
                items.push(this._generateScoreItem(Math.round(i*100)/100));
            }
            $(range).html(items.join(''));

            this.$_template.find('.year-start').text(this.$_minScore);
            this.$_template.find('.year-end').text(this.$_maxScore);
        },

        _generateScoreItem(score)
        {
            return `<div class="year-item" data-score="${score}"><span>${score}</span></div>`;
        },

        _generateSelectedClass()
        {
            let range = this.$_template.find('.year-ranges')
            range.find('.year-item').removeClass('selected inRange startRange endRange single')

            if (!this.$_startRange && !this.$_endRange) {
                return;
            }

            if (this.$_startRange) {
                const extra = !this.$_endRange ? 'single' : '';
                range.find(`.year-item[data-score="${this.$_startRange}"]`).addClass(`selected startRange ${extra}`)
            }

            if (this.$_endRange) {
                range.find(`.year-item[data-score="${this.$_endRange}"]`).addClass('selected endRange')
            }

            if (this.$_startRange && this.$_endRange) {
                for (let i = this.$_startRange; i < this.$_endRange; i+=0.1) {
                    if (i === this.$_startRange || i === this.$_endRange) {
                        continue;
                    }
                    range.find(`.year-item[data-score="${i}"]`).addClass('inRange')
                }
            }
        },
 
        _setElementValue()
        {
            let value = [this.$_startRange, this.$_endRange];
            this.$_element.val(value.join(' - '))
            this.$_element.trigger('change');
        },

        _parseElementValue()
        {
            let value = this.$_element.val();
            let extracts = value.split(' - ');
            console.log(extracts)
            if (extracts.length <= 0) {
                return;
            }

            let startRange = null;
            let endRange = null;
            if (extracts.length >= 1) {
                startRange = parseFloat(extracts[0] || 0) < 10 ? parseFloat(extracts[0] || 0) : null;
                endRange = parseFloat(extracts[1] || 0) > startRange ? parseFloat(extracts[1] || 0) : null;

            }
            this.$_startRange = startRange;
            this.$_endRange = endRange;
        }
    });
    $.fn[PLUGIN_NAME] = function (options) {
        this.each(function () {
            if (!$.data(this, "plugin_" + PLUGIN_NAME)) {
                $.data(this, "plugin_" + PLUGIN_NAME, new Plugin(this, options));
            }
        });
        return this;
    }; 
    $.fn[PLUGIN_NAME].defaults = {
        property  : 'value',
        onComplete: null
    };
})(jQuery, window, document);


$(document).ready(function () {
  $('.score-picker').scorepicker()
})