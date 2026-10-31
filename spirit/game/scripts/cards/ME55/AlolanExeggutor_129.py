from spirit.game.card_effects.support_common import heal_attack
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.scripts.cards.ME55.AlolanExeggutor_2 import ScaleUpPassive

card = PokemonCardDef(
    guid="42928aeb-a889-53cb-972e-df9c8c07c8b2",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name",
    display_name="Alolan Exeggutor",
    searchable_by=["Alolan Exeggutor", "Stage 1", "AlolanExeggutor"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Ability(
            title="Scale Up",
            game_text="If this Pok\u00e9mon has 6 or more Grass Energy attached, it gets +250 HP.",
            passive=ScaleUpPassive(),
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 50 damage from this Pok\u00e9mon",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=heal_attack(amount=50, target="self"),
        ),
    ],
)