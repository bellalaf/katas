## Kata01: Supermarket Pricing

So, what's the point of this? Honestly, I just want a structured way to play with code and logic, and keep up my lazyvim knowledge whilst I'm on a mini career break.

#### The problem

Some things in supermarkets have simple prices: this can of beans costs $0.65. Other things have more complex prices. For example:

- three for a dollar (so what’s the price if I buy 4, or 5?)
- $1.99/pound (so what does 4 ounces cost?)
- buy two, get one free (so does the third item have a price?)

This kata involves no coding. The exercise is to experiment with various models for representing money and prices that are flexible enough to deal with these (and other) pricing schemes, and at the same time are generally usable (at the checkout, for stock management, order entry, and so on). Spend time considering issues such as:

- does fractional money exist?
- when (if ever) does rounding take place?
- how do you keep an audit trail of pricing decisions (and do you need to)?
- are costs and prices the same class of thing?
- if a shelf of 100 cans is priced using “buy two, get one free”, how do you value the stock?

### Thoughts

##### Givens

Lets put all money into the smallest units, so that it is _always_ stored as an `int`. No messing with floating point nonsense, thank you. So, $1.99 would be stored as 199 cents.
Anything can be converted to the display currency (right align 2) at a BFF or even just FE layer if needed.

Rounding only happens at payment if the customer pays in cash. `int`s help here too. eg. at checkout if it's $1.99, obviously it's $2. But if someone has 5x $1.99, we are at $9.95 so we don't need to round.

We're going to need a pricing table and service. Something has a unit cost, but it might also have a 'what did we actually spend on this' cost, what it's expected to sell for, what it's valued at (insurance purposes maybe? ie. how much is your stock worth rn) etc.

##### Interesting bits

Okay, so the more fun stuff in this would be within the pricing service. So at checkout, any item entered would have it's default unit price shown, but it would also need to be checking for deals all the time.

```
get_checkout_price():
  if (this.buy_and_save() && this.quantity >= this.buy_and_save().get_qty()) {
    return this.buy_and_save().calculate()
}
```

Hmmm okay but the calculate would need to do some kind of floor. Like if it's 3 for 100 cents, and you had 4, I imagine it would pass in 4/3 and know there's one leftover. Also, are you allowed to have multiples of a discount? Is that shop wide or product by product. Buy and save needs to store/know that info too.

##### Valuing stock

I find this interesting. I'd be tempted to employ some kind of algorithm to each month do some kind of calculation to determine what the expected sell cost _per item_ is. So if people the past month have been only buying a 'buy 2, get 1 free' in groups of 3, I'd want to account for that. But even if something has a deal like that, it may not be used. Eg. a TV might be 'buy 1, get one half price', but how often do people actually buy two TVs at once? I'd want some historical data in there but also projected sales. Eg. going into the Xmas period, prawns are more likely to be bought by the kilo compared to in June (maybe?). Data pls. At a bare minimum, you would just do the unit price and perhaps at a store level, you'd know 'okay we tend to have 10% of reductions due to sales' and kind of account for it that way?

```

```
