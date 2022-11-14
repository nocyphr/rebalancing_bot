@given(u'an API')
def step_impl(context):
    context.base_url = 'localhost'
    

@given(u'an API key')
def step_impl(context):
    context.key = 'testkey'

@when(u'I check for balance')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I check for balance')


@then(u'I receive historical datetimes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I receive historical datetimes')


@then(u'I receive historical usd-balances')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I receive historical usd-balances')


@then(u'I receive historical crypto-balances')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I receive historical crypto-balances')


@when(u'I check for actions')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I check for actions')


@then(u'I receive historical crypto-amounts')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I receive historical crypto-amounts')


@then(u'I receive historical prices')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I receive historical prices')


@when(u'I check for transactions')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I check for transactions')


@then(u'I receive historical crypto-amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I receive historical crypto-amount')


@then(u'I receive historical usd-amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I receive historical usd-amount')


@given(u'I received a signal')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I received a signal')
