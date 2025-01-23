def generate_report():
    report = {
        'static_analysis': {
            'max_stress': max_stress,
            'max_deformation': max_deformation,
            'safety_factor': safety_factor
        },
        'modal_analysis': {
            'natural_frequencies': natural_freq_list,
            'mode_shapes': mode_shapes
        },
        'frequency_response': {
            'critical_frequencies': critical_freq,
            'max_accelerations': max_accel
        }
    }
    
    # レポートのHTML生成
    generate_html_report(report) 