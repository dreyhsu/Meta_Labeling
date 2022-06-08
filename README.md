# Meta_Labeling
Meta_Labeling is a project base on a book "Advances in Financial Machine Learning" by López de Prado.

<img src="https://user-images.githubusercontent.com/44833308/172560332-825bbd68-445d-4d35-a4b5-ac2d9fb74140.png" alt="Meta_Labeling" width="600"/>

The most powerful application if it is that it can determine the size of the bet. When we decide to trade commodities or stocks based on our own entry conditions (here, we called the entry condition as the Primary model), we can apply the success rate model (here we call the model as Meta-label) to predict the success rate of a trade , which also determines the size of the bet.

I apply this great method to develop my mid term ( 5~7 days ) long position trading strategy.
My Primary model : go long under two conditions (day timeframe):
1. low price touch the lower band ( for mean reversing )
2. high price touch the upper band ( for trend following )

But the problem is:
1. Many stocks in the profolio will mach the entry conditions, to invest in all the matched stocks is inefficient.
2. We can add more filters to narrow down the scope, but how to find the filter?

My Solution:
1. Filter stocks by implementing Meta_Labeling, and only trade the opportunity which success rate is over .9
2. Use Feature Selection to figure out the important features and add them to my entry condition.

- __[Notion](https://www.notion.so/BBand-mean-reversing-Strategy-ML-Threshold-Analysis-86c55d88d6734ec584800081c432f856)__ - Please check out the performance of this method under different entry points and win/loss ratio by my Notion page

