import "../../toy.wdl" as toy

workflow plot {
    File before_trimming
    File after_trimming
    String bar_color = 'white'
    String flier_color = 'grey'
    String plot_color = 'darkgrid'
    
    call toy.plot as plot { input:
        before_trimming = before_trimming,
        after_trimming = after_trimming,
        bar_color = bar_color,
        flier_color = flier_color,
        plot_color = plot_color
    }

    output {
        File plot_output = plot.plot_output
    }
}