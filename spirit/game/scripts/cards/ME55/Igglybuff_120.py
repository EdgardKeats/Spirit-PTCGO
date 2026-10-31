from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63ff93ad-7974-50b2-a3cb-6b55ec851448",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Basic", "Igglybuff"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=174,
    abilities=[
        Attack(
            title="Bouncy Circle",
            game_text="This attack does 30 damage for each of your Benched Pok\u00e9mon that has a maximum HP of 30.",
            cost={},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)