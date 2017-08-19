# Yosemitepaper
Nowadays, low latency and high throughput are required by data center applications. Coflow has been proposed as a new abstraction to capture the communication patterns in a rich set of data parallel applications, so that their application-level semantics can be effectively modeled. By taking coflows, instead of flows or packets, as the basic elements in network resource allocation or scheduling, application-level optimization goals such as reducing the coflow completion time (CCT) or application transfer latency can be better achieved. Although efficient coflow scheduling methods have been studied in this aspect, in this paper, we propose {\em weighted coflows} as a further step in this direction, where weights are used to express the importance or priorities of different coflows or applications, and weighted coflow completion time (WCCT) is set as the optimization target. We design and implement Yosemite, a system that aims to minimize WCCT by dynamically scheduling coflows according to their weights and the instantaneous network condition. We test Yosemite’s performance against several flow or coflow scheduling methods, by trace-driven simulations as well as real delopyment in a cloud testbed. Our trace-driven simulations show that, Yosemite's online scheduling algorithm performs about 20\%-50\% and 30\%-60\% better than that of Varys and Aalo, two state-of-the-art coflow scheduling systems, respectively. And in our testbed evaluations, Yosemite respectively achieves 30\% and 35\% average improvement against Varys and Aalo.# YosemitePaper2
