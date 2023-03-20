from .model import Type, TypeMobile
from typing import Optional, Any
from pydantic import Field


class SubscriptionState(Type):
    is_blocked: bool = Field(None, alias='isBlocked')
    is_trial: bool = Field(None, alias='isTrial')
    is_cancelled: bool = Field(None, alias='isCancelled')
    trial_already_used: bool = Field(None, alias='trialAlreadyUsed')
    is_processing: bool = Field(None, alias='isProcessing')


class UserInfo(Type):
    user_id: int = Field(None, alias='userId')
    first_name: str = Field(None, alias='firstName')
    middle_name: str = Field(None, alias='middleName')
    last_name: str = Field(None, alias='lastName')
    status: str
    expiration_date: Any = Field(None, alias='expirationDate')
    subscription_type: Any = Field(None, alias='subscriptionType')
    subscription_state: SubscriptionState = Field(None, alias='subscriptionState')
    is_auto_renew: Any = Field(None, alias='isAutoRenew')
    apple_subscription_state: Any = Field(None, alias='appleSubscriptionState')
    google_subscription_state: Any = Field(None, alias='googleSubscriptionState')


class AvailableAppleProducts(Type):
    monthly: str
    yearly: str


class AvailableGoogleProducts(Type):
    monthly: str
    yearly: str


class SubscriptionInfoResponse(TypeMobile):
    user_info: Optional[UserInfo] = Field(None, alias='userInfo')
    family_info: Optional[Any] = Field(None, alias='familyInfo')
    available_apple_products: Optional[AvailableAppleProducts] = Field(
        None, alias='availableAppleProducts'
    )
    available_google_products: Optional[AvailableGoogleProducts] = Field(
        None, alias='availableGoogleProducts'
    )
    is_simple_labels: Optional[bool] = Field(None, alias='isSimpleLabels')
